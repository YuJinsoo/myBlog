from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager # django의 인증기능이 적용된 모델
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, username, password, email, is_staff, is_superuser, **extra_fields):
        if not username:
            raise ValueError('User must have an username')
        now = timezone.now() # 현재시간 -> UTC
        # now = timezone.localtime() # 현재 위치 시간으로 기록됨
        email = self.normalize_email(email)
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_active = True,
            is_superuser = is_superuser,
            last_login = now,
            date_joined = now
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
        
    # BaseUserManger함수 1 : create_user
    def create_user(self, username, password, email, **extra_fields):
        return self._create_user(username, password, email, False, False, **extra_fields)
    
    # BaseUserManger함수 2 : create_superuser
    def create_superuser(self, username, password, email, **extra_fields):
        return self._create_user(username, password, email, True, True, **extra_fields)

    
class User(AbstractUser):
    # 한 테이블에 unique는 1개만 있을 수 있습니다.
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True, max_length=255)
    
    # null과 blank 허용
    name = models.CharField(max_length=50, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateField(null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    
    objects = UserManager()
    