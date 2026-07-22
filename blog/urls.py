from django.urls import path

from .views import (
    AboutView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    search_authors,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('acerca-de/', AboutView.as_view(), name='about'),
    path('autores/buscar/', search_authors, name='author_search'),
    path('posts/nuevo/', PostCreateView.as_view(), name='post_create'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<slug:slug>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<slug:slug>/eliminar/', PostDeleteView.as_view(), name='post_delete'),
]
