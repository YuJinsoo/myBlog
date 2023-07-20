from django import forms
from .models import Post, Comment, ReComment, Category


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category']
        widgets ={
            'title':forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'category':forms.Select(attrs={
                'class': 'form-control'
                }),
            'content':forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'width:100%;'
                }),
            'image':forms.FileInput(attrs={
                'class': 'form-control'
                })
            }


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