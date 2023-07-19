# user를 auth를 사용해서 개발했으니 폼도 auth에서 제공하는 form을 사용해야 합니다.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model  

User = get_user_model()


class RegisterForm(UserCreationForm):
    
    class Meta():
        model = User
        fields = ['username', 'email']


class LoginForm(AuthenticationForm):
    
    class Meta():
        model = User
        fields = ['username', 'password']
        # widget = {
        #     'email': forms.EmailField(attrs={'placeholder':'email'}),
        #     'password': forms.PasswordInput(attrs={'placeholder':'password'})
        # }