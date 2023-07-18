from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import Q
from .models import Post, Comment, Category
from .forms import PostForm


class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        category = Category.objects.all()
        context = {
            "posts": posts,
            "category": category
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
    

# search url 규칙을 맞추기 위해 요청만 보냄.
class PostSearchQuery(View):
    def get(self, request):
        print(request)
        print(request.GET)
        cat = request.GET.get('cat')
        if cat == '':
            cat = 'All'
            return redirect('blog:list')
        print(cat)
        return redirect('blog:search', cat=cat)
    
    
class PostSearch(View):
    def get(self, request, cat):
        ## 단일 카테고리에 일치하는 것만 검색
        # TODO 추후 여러개, 제목/내용/작성자 에 대한 검색, 대소문자 고려해보기
        if cat == 'etc':
            posts =  Post.objects.filter(category=None)
        else:
            category = Category.objects.filter(name=cat)
            
            if len(category) > 0:
                posts =  Post.objects.filter(category=category[0])
            else:
                posts = None

        context = {
            'posts' : posts,
            'searchtag': cat,
        }
        return render(request, 'blog/post_list.html', context=context)