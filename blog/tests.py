from django.contrib.auth.models import User
from django.template import Context, Template
from django.test import TestCase
from django.urls import reverse

from .forms import PostForm
from .context_processors import site_info
from .models import Author, Post, Tag


class PostModelTests(TestCase):
    def test_published_posts_manager_returns_only_published_posts(self):
        author = User.objects.create_user(username='autor', password='clave-segura')
        published = Post.objects.create(
            title='Entrada visible',
            subtitle='Subtitulo visible',
            content='Contenido suficientemente claro para publicar.',
            author=author,
            published=True,
        )
        Post.objects.create(
            title='Borrador',
            subtitle='Subtitulo oculto',
            content='Contenido privado.',
            author=author,
            published=False,
        )

        self.assertEqual(list(Post.published_posts.all()), [published])

    def test_slug_is_generated_from_title(self):
        author = User.objects.create_user(username='autor', password='clave-segura')
        post = Post.objects.create(
            title='Mi Primera Entrada',
            subtitle='Subtitulo',
            content='Contenido suficientemente claro para publicar.',
            author=author,
        )

        self.assertEqual(post.slug, 'mi-primera-entrada')

    def test_post_can_have_author_profile_and_tags(self):
        user = User.objects.create_user(username='autor', password='clave-segura')
        author = Author.objects.create(name='Ana Bloguera', email='ana@example.com')
        tag = Tag.objects.create(name='Django')
        post = Post.objects.create(
            title='Entrada con etiquetas',
            subtitle='Subtitulo',
            content='Contenido suficientemente claro para publicar.',
            author=user,
            author_profile=author,
        )
        post.tags.add(tag)

        self.assertEqual(post.author_profile, author)
        self.assertEqual(list(post.tags.all()), [tag])


class PostFormTests(TestCase):
    def test_post_form_rejects_short_content(self):
        form = PostForm(
            data={
                'title': 'Titulo valido',
                'subtitle': 'Subtitulo valido',
                'content': 'corto',
                'published': True,
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)


class TemplateUtilityTests(TestCase):
    def test_site_info_context_processor_exposes_blog_name(self):
        self.assertEqual(site_info(None)['site_name'], 'MiblogFinal')

    def test_format_date_filter_formats_date(self):
        rendered = Template(
            "{% load blog_filters %}{{ value|format_date }}"
        ).render(Context({'value': __import__('datetime').date(2026, 7, 9)}))

        self.assertEqual(rendered, '09/07/2026')


class BlogViewTests(TestCase):
    def test_post_list_shows_published_post_titles(self):
        author = User.objects.create_user(username='autor', password='clave-segura')
        Post.objects.create(
            title='Entrada publica',
            subtitle='Subtitulo',
            content='Contenido suficientemente claro para publicar.',
            author=author,
            published=True,
        )
        Post.objects.create(
            title='Entrada privada',
            subtitle='Subtitulo',
            content='Contenido suficientemente claro para publicar.',
            author=author,
            published=False,
        )

        response = self.client.get(reverse('post_list'))

        self.assertContains(response, 'Entrada publica')
        self.assertNotContains(response, 'Entrada privada')

    def test_anonymous_user_cannot_open_post_create_page(self):
        response = self.client.get(reverse('post_create'))

        self.assertRedirects(response, f"{reverse('login')}?next={reverse('post_create')}")

    def test_author_can_update_own_post(self):
        author = User.objects.create_user(username='autor', password='clave-segura')
        post = Post.objects.create(
            title='Titulo anterior',
            subtitle='Subtitulo',
            content='Contenido suficientemente claro para publicar.',
            author=author,
            published=True,
        )
        self.client.login(username='autor', password='clave-segura')

        response = self.client.post(
            reverse('post_update', kwargs={'slug': post.slug}),
            {
                'title': 'Titulo nuevo',
                'subtitle': 'Subtitulo nuevo',
                'content': 'Contenido actualizado con suficiente longitud.',
                'published': True,
            },
        )

        post.refresh_from_db()
        self.assertRedirects(response, reverse('post_detail', kwargs={'slug': post.slug}))
        self.assertEqual(post.title, 'Titulo nuevo')

    def test_duplicate_post_submit_reuses_recent_existing_post(self):
        author = User.objects.create_user(username='autor', password='clave-segura')
        self.client.login(username='autor', password='clave-segura')
        data = {
            'title': 'Entrada duplicada',
            'subtitle': 'Subtitulo duplicado',
            'content': 'Contenido suficientemente largo para publicar una entrada.',
            'published': True,
        }

        first_response = self.client.post(reverse('post_create'), data)
        second_response = self.client.post(reverse('post_create'), data)

        post = Post.objects.get(title='Entrada duplicada')
        self.assertRedirects(first_response, reverse('post_detail', kwargs={'slug': post.slug}))
        self.assertRedirects(second_response, reverse('post_detail', kwargs={'slug': post.slug}))
        self.assertEqual(Post.objects.filter(title='Entrada duplicada').count(), 1)

    def test_non_author_cannot_update_post(self):
        author = User.objects.create_user(username='autor', password='clave-segura')
        other = User.objects.create_user(username='otro', password='clave-segura')
        post = Post.objects.create(
            title='Entrada del autor',
            subtitle='Subtitulo',
            content='Contenido suficientemente claro para publicar.',
            author=author,
            published=True,
        )
        self.client.login(username='otro', password='clave-segura')

        response = self.client.get(reverse('post_update', kwargs={'slug': post.slug}))

        self.assertEqual(response.status_code, 403)

    def test_search_authors_returns_matching_author(self):
        Author.objects.create(name='Ana Bloguera', email='ana@example.com')
        Author.objects.create(name='Carlos Editor', email='carlos@example.com')

        response = self.client.get(reverse('author_search'), {'q': 'Ana'})

        self.assertContains(response, 'Ana Bloguera')
        self.assertNotContains(response, 'Carlos Editor')
