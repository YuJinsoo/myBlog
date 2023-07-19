from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    # 회원가입
    path("register/", views.Register.as_view(), name="register"),
    # 로그인요청
    path("login/", views.Login.as_view(), name="login"),
    # 로그아웃요청
    path("logout/", views.Logout.as_view(), name="logout"),
    
]
