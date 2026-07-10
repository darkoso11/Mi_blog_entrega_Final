from django.urls import path

from . import views

urlpatterns = [
    path('registro/', views.register, name='register'),
    path('perfil/', views.profile, name='profile'),
    path('perfil/editar/', views.profile_edit, name='profile_edit'),
]
