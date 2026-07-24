from django import forms

from .models import Author, Post, Tag
from .utils import sync_author_for_user


class PostForm(forms.ModelForm):
    tag_names = forms.CharField(
        label='Etiquetas',
        required=False,
        help_text='Escribe etiquetas separadas por coma. Ejemplo: Django, Recetas, Viajes',
    )

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'author_profile', 'tag_names', 'image']
        labels = {
            'title': 'Titulo',
            'subtitle': 'Subtitulo',
            'content': 'Contenido',
            'author_profile': 'Autor',
            'image': 'Imagen',
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            author = sync_author_for_user(user)
            self.fields['author_profile'].initial = author.pk
        self.fields['author_profile'].queryset = Author.objects.all()
        self.fields['author_profile'].required = True
        if self.instance.pk:
            self.fields['tag_names'].initial = ', '.join(
                self.instance.tags.values_list('name', flat=True)
            )

    def clean_content(self):
        content = self.cleaned_data['content'].strip()
        if len(content) < 20:
            raise forms.ValidationError('El contenido debe tener al menos 20 caracteres.')
        return content

    def _save_m2m(self):
        super()._save_m2m()
        tag_names = self.cleaned_data.get('tag_names', '')
        tags = []
        for name in [tag.strip() for tag in tag_names.split(',') if tag.strip()]:
            tag, _created = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        self.instance.tags.set(tags)
