from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'author_profile', 'tags', 'image', 'published']
        labels = {
            'title': 'Titulo',
            'subtitle': 'Subtitulo',
            'content': 'Contenido',
            'author_profile': 'Autor',
            'tags': 'Etiquetas',
            'image': 'Imagen',
            'published': 'Publicado',
        }
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }

    def clean_content(self):
        content = self.cleaned_data['content'].strip()
        if len(content) < 20:
            raise forms.ValidationError('El contenido debe tener al menos 20 caracteres.')
        return content
