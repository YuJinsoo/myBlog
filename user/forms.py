# user를 auth를 사용해서 개발했으니 폼도 auth에서 제공하는 form을 사용해야 합니다.
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model  
from .models import Profile

from datetime import date

User = get_user_model()


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = ['username', 'email', 'password1', 'password2']
        for f in fields:
            self.fields[f].widget.attrs.update({'class':'form-control'})
            
    class Meta():
        model = User
        fields = ['username', 'email']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = ['username', 'password']
        for f in fields:
            self.fields[f].widget.attrs.update({'class':'form-control'})
        
    class Meta():
        model = User
        fields = ['username', 'password']
        ## 위젯 적용이 안됨.. 왜지?
        ## Authentication Form에서 미리 지정해버리기 때문에
        ## 생성자를 오버라이드함
        widgets = {
            'username': forms.TextInput(
                attrs={
                    "class": "form-control",
                    'placeholder': '아이디'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '비밀번호'
                }
            )
        }
        # widget = {
        #     'email': forms.EmailField(attrs={'placeholder':'email'}),
        #     'password': forms.PasswordInput(attrs={'placeholder':'password'})
        # }


class DateInput(forms.DateInput):
    input_type='date'


class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['user', 'nickname', 'birthday', 'profile_image']
        widgets = {
            'nickname': forms.TextInput(
                attrs={
                    "class": "form-control",
                    'placeholder': '별명 50자'
                }
            ),
            'birthday': DateInput(
                attrs={
                    'class': 'form-control',
                    # 'placeholder': '생년월일'
                }
            ),
            'profile_image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }