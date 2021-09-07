from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from notebook_app.models import Note, Todo


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['heading', 'content']


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']


class EditTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['heading', 'content']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
