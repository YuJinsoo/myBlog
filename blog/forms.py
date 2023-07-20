from django import forms
from .models import Post, Comment, ReComment, Category


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':'3', 'cols':'50'})
        }


class ReCommentForm(forms.ModelForm):
    
    class Meta:
        model = ReComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':'3', 'cols':'40'})
        }