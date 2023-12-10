from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['title', 'author', 'categoryType', 'postCategory', 'text']

   def clean(self):
       cleaned_data = super().clean()
       title = cleaned_data.get("title")
       text = cleaned_data.get("text")

       if title == text:
           raise ValidationError(
               "Текст статьи не должен быть идентичен заголовку."
           )
       return cleaned_data