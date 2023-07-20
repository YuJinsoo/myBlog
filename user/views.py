from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, RegisterForm


class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = RegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'user/user_register.html', context=context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            return redirect("user:login")
        
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form,
        }
        return render(request, 'user_register.html', context=context)


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        # togo = None
        
        # if "next" in request.GET.keys() :
        #     togo = "/"+"/".join(request.GET["next"].split("/")[1:4])
            
        form = LoginForm()
        context = {
            'form':form,
            # 'togo': togo
        }
        return render(request, 'user/user_login.html', context=context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            passsword = form.cleaned_data['password']
            
            user = authenticate(username = username, password=passsword)
            if user:
                login(request, user)
                
                return redirect('blog:list')
        
        form.add_error(None, '아이디가 없습니다.')
        context = {
            'form':form
        }
        return redirect('blog:list')


class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            print('Bye~')
            logout(request)
        
        return redirect('/')


class MyPage(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context = {
            'user': user,
        }
        return render(request, 'user/user_mypage.html', context=context)