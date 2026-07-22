from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Author, Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.published_posts.select_related('author', 'author_profile').prefetch_related('tags')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Post.objects.select_related('author', 'author_profile').prefetch_related('tags')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        recent_cutoff = timezone.now() - timezone.timedelta(seconds=30)
        duplicate = Post.objects.filter(
            author=self.request.user,
            title=form.cleaned_data['title'],
            subtitle=form.cleaned_data['subtitle'],
            content=form.cleaned_data['content'],
            created_at__gte=recent_cutoff,
        ).first()
        if duplicate:
            messages.info(self.request, 'La entrada ya habia sido guardada.')
            return redirect(duplicate.get_absolute_url())
        form.instance.author = self.request.user
        messages.success(self.request, 'La entrada fue creada correctamente.')
        return super().form_valid(form)


class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.is_staff


class PostUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, 'La entrada fue actualizada.')
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def form_valid(self, form):
        messages.success(self.request, 'La entrada fue eliminada.')
        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'blog/about.html'


def search_authors(request):
    query = request.GET.get('q', '').strip()
    results = Author.objects.filter(name__icontains=query) if query else Author.objects.all()
    return render(
        request,
        'blog/search_authors.html',
        {'query': query, 'results': results},
    )
