from django import forms
from .models import Post, Comment, ReComment, Category


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'style' : 'height:4em',
                'class':'form-control'
                })
        }


class ReCommentForm(forms.ModelForm):
    
    class Meta:
        model = ReComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'style' : 'height:4em',
                'class':'form-control'})
        }