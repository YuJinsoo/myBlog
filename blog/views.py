from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
# from django.db.models import Q

# auth의 mixin 기능
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import date, datetime, timedelta

from .models import Post, Comment, Category, ReComment
from .forms import PostForm, CommentForm, ReCommentForm



class PostList(View):
    def get(self, request):
        post_list = Post.objects.all().order_by('-created_at')
        query_pagenum = request.GET.get('page')
        
        posts_num = len(post_list)
        categories = Category.objects.all()
        cat_null_posts = Post.objects.filter(category__isnull=True)
        
        paginator = Paginator(post_list, 4)
        
        # 페이지 수 에러처리.
        try:
            posts = paginator.get_page(query_pagenum)
        except PageNotAnInteger:
            query_pagenum = 1
            posts = paginator.get_page(query_pagenum)
        except EmptyPage:
            query_pagenum = paginator.num_pages
            posts = paginator.get_page(query_pagenum)
            
        total_page = paginator.num_pages
        context = {
            "post_list": post_list,
            "posts_num": posts_num,
            "categories": categories,
            "posts" : posts,
            "cat_null_posts": cat_null_posts,
            "paginator": paginator,
        }
        # return render(request, "blog/post_list.html", context=context)
        return render(request, "blog/post_list.html", context=context)


class PostDetail(View):
    def get(self, request, post_id):        
        # 404발생 즉시 중단되고 404를 출력해줌
        post = get_object_or_404(Post, pk= post_id)
        comments = Comment.objects.filter(post=post).order_by("-created_at")
        comment_form = CommentForm()
        recomment_form = ReCommentForm()
        context = {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
            "recomment_form": recomment_form
        }
        
        # HttpResponse 생성
        response = render(request, "blog/post_detail.html", context=context)
        
        # 쿠키 만료기간 설정을 위한 셋
        expire_date, now = datetime.now(), datetime.now()
        expire_date += timedelta(hours=1)
        expire_date -= now
        max_age = expire_date.total_seconds()

        # 클라이언트의 쿠키 얻기
        cookie_value = request.COOKIES.get('hitpost', '_')
        
        if f'_{post_id}_' not in cookie_value:
            cookie_value += f'{post_id}_'
            # python에서 쿠키생성 set_cookie(쿠키이름, 값, 만료기간, js접근불가능)
            # 쿠키가 없으면 생성, 있으면 추가하는 메서드
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
            if request.FILES:
                print(request.FILES['image'])
                post.image = request.FILES['image']
            post.save()
            return redirect('blog:list')
        
        # form.add_error(None, '폼이 유효하지 않습니다.') # 에러 전달도 해줘야함
        return redirect('blog:write')


class PostEdit(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        # print(post.image)
        form = PostForm(initial={'title':post.title, 'content':post.content, 'category': post.category, 'author': post.author, 'image': post.image })
        
        context = {
            'post': post,
            'form': form
        }
        return render(request, "blog/post_edit.html", context=context)
    
    def post(self, request, post_id):
        post =Post.objects.get(pk=post_id)
        checked = request.POST.getlist("cancel") # [] or ['1']
        if post.author == request.user or request.user.is_superuser:
            form = PostForm(request.POST, request.FILES)

            if form.is_valid():
                post.title = form.cleaned_data["title"]
                post.content = form.cleaned_data["content"]
                post.category = form.cleaned_data["category"]
                post.image = request.POST['originimage'] # form안 input들의 name이 key로, value는 value로 들어감.
                
                if request.FILES :
                    post.image = request.FILES['image']
                
                if bool(checked) :
                    post.image = None # None 들어가는거 맞겠지?
                    
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
## TODO - 거쳐가지 않고 한번에 가도록 수정해야 함.
# class PostSearchQuery(View):
#     def get(self, request):
#         print(request)
#         print(request.GET)
#         cat = request.GET.get('cat')
#         if cat == '':
#             cat = 'All'
#             return redirect('blog:list')
#         print(cat)
#         return redirect('blog:search', cat=cat)


class PostSearch(View):
    # TODO 추후 여러개, 제목/내용/작성자 에 대한 검색, 대소문자 고려해보기
    
    def get(self, request):
        qp = request.GET.get('search', None)
        query_pagenum = request.GET.get('page', None)
        
        if qp == None:
            return redirect('blog:list')
        else:
            search_result = Post.objects.filter(title__icontains=qp)
            print(search_result)
            
            posts_num = len(search_result)
            categories = Category.objects.all()
            cat_null_posts = Post.objects.filter(category__isnull=True)
            
            paginator = Paginator(search_result, 4)
            # 페이지 수 에러처리.
            try:
                posts = paginator.get_page(query_pagenum)
            except PageNotAnInteger:
                query_pagenum = 1
                posts = paginator.get_page(query_pagenum)
            except EmptyPage:
                query_pagenum = paginator.num_pages
                posts = paginator.get_page(query_pagenum)
                
            total_page = paginator.num_pages
            context = {
                "post_list": search_result,
                "posts_num": posts_num,
                "categories": categories,
                "posts" : posts,
                "cat_null_posts": cat_null_posts,
                "paginator": paginator,
                "qp": qp,
            }

            return render(request, "blog/post_list.html", context=context)
    


class CategorySearch(View):
    def get(self, request, cat):
        ## 단일 카테고리에 일치하는 것만 검색
        posts_num = Post.objects.count()
        categories = Category.objects.all()
        cat_null_posts = Post.objects.filter(category__isnull=True)
        if cat == "None":
            post_list =  Post.objects.filter(category=None).order_by('-created_at')
        else:
            category = Category.objects.filter(name=cat)
            
            if category:
                print("here!")
                post_list =  Post.objects.filter(category=category[0]).order_by('-created_at')
            else:
                post_list = None

        query_pagenum = request.GET.get('page', None)
        
        paginator = Paginator(post_list, 4)
        
        # 페이지 수 에러처리.
        try:
            posts = paginator.get_page(query_pagenum)
        except PageNotAnInteger:
            query_pagenum = 1
            posts = paginator.get_page(query_pagenum)
        except EmptyPage:
            query_pagenum = paginator.num_pages
            posts = paginator.get_page(query_pagenum)
        
        # print(posts, posts.number, len(posts))
        # print(query_pagenum, paginator.page_range, post_list, len(post_list))
        
        context = {
            "posts" : posts,
            "posts_num": posts_num,
            "searchtag": cat,
            "categories": categories,
            "cat_null_posts": cat_null_posts,
            "paginator": paginator,
        }
        return render(request, 'blog/post_list.html', context=context)
    

class CommentWrite(LoginRequiredMixin, View):
    def post(self, request, post_id):
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=post_id)
        
        if form.is_valid():
            content = form.cleaned_data['content']
            author = request.user
            
            comment = Comment.objects.create(post=post, content=content, author=author)
            
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


### 대댓글
class ReCommentWrite(LoginRequiredMixin, View):
    def post(self, request, post_id, cm_id):
        comment = get_object_or_404(Comment, pk=cm_id)
        form = ReCommentForm(request.POST)
        author = request.user
        
        if form.is_valid():
            content = form.cleaned_data["content"]
            recm = ReComment.objects.create(comment=comment, author=author, content=content)
            
        return redirect('blog:detail', post_id=post_id)


class ReCommentDelete(LoginRequiredMixin, View):
    def post(self, request, post_id, rcm_id):
        rcm = get_object_or_404(ReComment, pk=rcm_id)
        rcm.delete()
        return redirect('blog:detail', post_id=post_id)


# 404 error handler
def page_not_found(request, exception):
    return render(request, 'blog/404.html')


