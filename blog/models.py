from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

## auth를 확장된 모델을 가져오게 됩니다.
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"[{self.pk}] {self.title} :: {self.author} - {self.created_at}"


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    


class ReComment(models.Model):
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("blog:search-category", kwargs={"cat": self.name})
    