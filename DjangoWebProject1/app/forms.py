"""
Definition of forms.
"""

from importlib.metadata import requires
from random import choice
from turtle import width
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class MessageForm(forms.Form):    
    name = forms.CharField(label='Ваше имя')
    msg = forms.CharField(label='Ваше сообщение',
                              widget=forms.Textarea(attrs={'rows':12, 'cols':26}))
    rate = forms.ChoiceField(label='Ваша оценка',
                             choices=(('1','1'),
                             ('2','2'),
                             ('3','3')), initial=1)
    ans = forms.BooleanField(label='Отправить на e-mail',
                             required=False)
    email = forms.EmailField(label='e-mail')

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image', )
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}