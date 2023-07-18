from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Post, Comment
from .forms import PostForm


class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            "posts": posts,
        }
        return render(request, "blog/post_list.html", context=context)


class PostDetail(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk= post_id)
        context = {
            "post": post,
        }
        return render(request, "blog/post_detail.html", context=context)


class PostWrite(View):
    def get(self, request):
        form = PostForm()
        context = {
            "form":form,
        }
        return render(request, "blog/post_write.html", context=context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user # TODO 글 저자를 로그인한 유저로 변경해야 함.
            post.save()
            return redirect('blog:list')
        
        # form.add_error(None, '폼이 유효하지 않습니다.') # 에러 전달도 해줘야함
        return redirect('blog:write')

class PostEdit(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(initial={'title':post.title, 'content':post.content, 'category': post.category, 'author': post.author})
        context = {
            'post': post,
            'form': form
        }
        return render(request, "blog/post_edit.html", context=context)
    
    def post(self, request, post_id):
        post =Post.objects.get(pk=post_id)
        form = PostForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            post.title = form.cleaned_data["title"]
            post.content = form.cleaned_data["content"]
            post.category = form.cleaned_data["category"]
            post.save()
            return redirect('blog:detail', post_id=post_id)
        
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context=context)
    
    
class PostDelete(View):
    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('blog:list')