from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, RegisterForm, ProfileForm
from .models import Profile

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
        profile_form = ProfileForm()
        profile = None
        
        if hasattr(user, "profile"):
            profile = user.profile
            profile_form = ProfileForm(initial={
                'user': profile.user,
                'nickname': profile.nickname, 
                'birthday': profile.birthday,
                'profile_image': profile.profile_image
            })
            
        context = {
            'user': user,
            'profile_form': profile_form,
            'profile': profile
        }
        return render(request, 'user/user_mypage.html', context=context)


class EditProfile(LoginRequiredMixin, View):
    def post(self, request):
        nickname = request.POST['nickname']
        birthday = request.POST['birthday']
        print(request.POST['birthday'])
            
        if request.POST["type"] == "create":
            profile_image = None
            if hasattr(request.FILES, 'profile_image'):
                profile_image = request.FILES['profile_image']
            Profile(user=request.user, nickname=nickname, birthday=birthday, profile_image=profile_image).save()
        else:
            profile = get_object_or_404(Profile, user=request.user)
            profile.nickname = request.POST['nickname']
            profile.birthday = request.POST['birthday']
            if hasattr(request.FILES,'profile_image'):
                profile.profile_image= request.FILES['profile_image']
            
            profile.save()
            
        return redirect('user:mypage')


# class EditProfile(LoginRequiredMixin, View):
#     def post(sefl, request):
#         profile = get_object_or_404(Profile, user=request.user)
#         profile.nickname = request.POST['nickname']
#         profile.birthday = request.POST['birthday']
#         profile.profile_image = request.POST['profile_image']
        
#         return redirect('uset:mypage')