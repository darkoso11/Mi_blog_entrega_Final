from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name='blog_author',
        blank=True,
        null=True,
    )
    name = models.CharField('nombre', max_length=100)
    email = models.EmailField('email', unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('nombre', max_length=30, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)


class Post(models.Model):
    title = models.CharField('titulo', max_length=120)
    slug = models.SlugField('slug', max_length=140, unique=True, blank=True)
    subtitle = models.CharField('subtitulo', max_length=180)
    content = models.TextField('contenido')
    image = models.ImageField('imagen', upload_to='posts/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    author_profile = models.ForeignKey(
        Author,
        verbose_name='autor del blog',
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(Tag, verbose_name='etiquetas', related_name='posts', blank=True)
    published = models.BooleanField('publicado', default=True)
    created_at = models.DateTimeField('creado', auto_now_add=True)
    updated_at = models.DateTimeField('actualizado', auto_now=True)

    objects = models.Manager()
    published_posts = PublishedPostManager()

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 2
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
