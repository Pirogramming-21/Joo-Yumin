from django import forms
from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']