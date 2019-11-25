from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, _user_has_perm
from django.core import validators
from django.conf import settings

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):    
        if not request_data['email']:
            raise ValueError('email 주소는 반드시 입력해야 합니다.')

        profile = ""
        if request_data.get('profile'):
            profile = request_data['profile']
        
        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            profile = profile
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        request_data = {
            'email': email,
            'username': username,
            'password': password
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True) # 닉네임
    email = models.EmailField(verbose_name='email 주소', max_length=255, unique=True)   # 이메일
    profile = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)   # 활성화
    is_staff = models.BooleanField(default=False)   # 권한
    is_admin = models.BooleanField(default=False)   # 권한

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)
    
    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'