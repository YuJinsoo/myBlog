from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# from django.db.models import Q

# auth의 mixin 기능
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, datetime, timedelta

from .models import Post, Comment, Category
from .forms import PostForm, CommentForm



class PostList(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        category = Category.objects.all()
        context = {
            "posts": posts,
            "category": category
        }
        return render(request, "blog/post_list.html", context=context)


class PostDetail(View):
    def get(self, request, post_id):        
        # 404발생 즉시 중단되고 404를 출력해줌
        post = get_object_or_404(Post, pk= post_id)
        comments = Comment.objects.filter(post=post).order_by("-created_at")
        comment_form = CommentForm()
        context = {
            "post": post,
            "comments": comments,
            "comment_form": comment_form
        }
        
        #
        #if post.author == request.user or request.user.is_superuser:
        #    pass
        # HttpResponse 생성
        response = render(request, "blog/post_detail.html", context=context)
        
        
        expire_date, now = datetime.now(), datetime.now()
        expire_date += timedelta(hours=1)
        expire_date -= now
        max_age = expire_date.total_seconds()

        # 클라이언트의 쿠키 얻기
        cookie_value = request.COOKIES.get('hitpost', '_')
        
        if f'_{post_id}_' not in cookie_value:
            cookie_value += f'{post_id}_'
            # python에서 쿠키생성 set_cookie(쿠키이름, 값, 만료기간, js접근불가능)
            response.set_cookie('hitpost', value=cookie_value, max_age=max_age, httponly=True)
            post.hits +=1
            post.save()
        
        return response


class PostWrite(LoginRequiredMixin, View):
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
            post.author = request.user
            post.save()
            return redirect('blog:list')
        
        # form.add_error(None, '폼이 유효하지 않습니다.') # 에러 전달도 해줘야함
        return redirect('blog:write')


class PostEdit(LoginRequiredMixin, View):
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
        
        if post.author == request.user or request.user.is_superuser:
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
        
        return redirect('blog:edit', post_id=post_id)


class PostDelete(LoginRequiredMixin, View):
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
            posts =  Post.objects.filter(category=None).order_by('-created_at')
        else:
            category = Category.objects.filter(name=cat)
            
            if len(category) > 0:
                posts =  Post.objects.filter(category=category[0]).order_by('-created_at')
            else:
                posts = None

        context = {
            'posts' : posts,
            'searchtag': cat,
        }
        return render(request, 'blog/post_list.html', context=context)
    

class CommentWrite(LoginRequiredMixin, View):
    def post(self, request, post_id):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=post_id)
        
        if form.is_valid():
            content = form.cleaned_data['content']
            author = request.user
            
            commnet = Comment.objects.create(post=post, content=content, author=author)
            
            return redirect("blog:detail", post_id=post_id)
        
        form.add_error('content','폼이 유효하지 않습니다.')
        context = {
            'post': post,
            'comments': post.comment_set.all(),
            'comment_form': form
        }
        return render(request, "blog/post_detailhtml", context=context)


class CommentDelete(LoginRequiredMixin, View):
    def post(self, request, cm_id):
        comment = get_object_or_404(Comment, pk=cm_id)
        print(comment)
        postid = comment.post.id
        comment.delete()
        return redirect('blog:detail', post_id=postid)

# 404 error handler
def page_not_found(request, exception):
    return render(request, 'blog/404.html')


