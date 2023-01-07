# 01. Custom User 생성 (email로 로그인)

## Custom User를 프로젝트 시작하기 전에 만드는 이유는, 나중에 수정하기 용이합니다. Project 중간에 User Model을 건드리기는 매우 힘듭니다. 따라서 Proejct 시작할 때 해주시는 것이 가장 좋습니다.
## 로그인 시에 username이 아닌 email을 사용하도록 변경할 예정입니다.
## Custom User 생성하기 앞서 아래와 같이 먼저 app을 추가해 줍니다.

## Terminal을 이용하여 accounts app 생성
```
python manage.py startapp accounts
```
## 생성된 앱을 `api/settings.py` 에 추가해줍니다.
## `api/settings.py` 에 앱 추가
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 새로 추가한 앱
    'accounts',
]
```
## 새로 만들 User model을 만들기 앞서 `accounts/managers.py` 에 User Manager를 추가해주고, User Model을 `accounts/models.py` 추가해줍니다.
## `accounts/managers.py` 추가
```
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
```
## `accounts/models.py`에 Custom User 추가
```
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
```
## 마지막으로 `api/settings.py` 에 사용하는 User 모델을 선언해줍니다.
## `pi/settings.py` 사용할 User 모델 선언
```
AUTH_USER_MODEL = 'accounts.User'
```
## 위 같이 설정해주면, User를 이용할 때 더 이상 username이 아닌 email을 사용하여 로그인 및 계정 생성을 진행할 수 있게 됩니다.

# 2. 라이브러리를 활용하여 회원가입 구현하기
## 우선 필요한 라이브러리들을 설치하도록 합니다.
## Terminal을 이용하여 추가 라이브러리 설치
```
# 라이브러리 설치
pip install djangorestframework dj-rest-auth django-allauth djangorestframework-simplejwt
```
## 설치한 라이브러리
- ## djangorestframework: Django를 REST API 형태로 사용할 수 있도록 도와줍니다.
- ## dj-rest-auth: REST API 형태로 제공해주는 로그인, 비밀번호 찾기 등의 기능을 제공합니다. (django-rest-auth라는 라이브러리가 더 이상 개발되지 않음에 따라 생긴 프로젝트)
- ## django-allauth: 회원가입 기능을 제공합니다.
- ## djangorestframework-simplejwt: Django에서 JWT Token을 사용하도록 도와줍니다.

## `api/settings.py` 에 새로 설치한 앱(Package) 추가
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 새로 추가한 앱
    'accounts',
    # 설치한 라이브러리들
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

SITE_ID = 1
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
```
## 설치한 라이브러리를 사용할 수 있도록 `api/settings.py` 에 추가해 줍니다.
## 변수 목록

## dj-rest-auth

- ## REST_USE_JWT: JWT 사용 여부
- ## JWT_AUTH_COOKIE: 호출할 Cookie Key값
- ## JWT_AUTH_REFRESH_COOKIE: Refresh Token Cookie Key 값 (사용하는 경우)

## django-allauth

- ## SITE_ID: 해당 도메인의 id (django_site 테이블의 id, oauth 글에서 다룰 예정)
- ## ACCOUNT_UNIQUE_EMAIL: User email unique 사용 여부
- ## ACCOUNT_USER_MODEL_USERNAME_FIELD: User username type
- ## ACCOUNT_USERNAME_REQUIRED: User username 필수 여부
- ## ACCOUNT_EMAIL_REQUIRED: User email 필수 여부
- ## ACCOUNT_AUTHENTICATION_METHOD: 로그인 인증 수단
- ## ACCOUNT_EMAIL_VERIFICATION: Email 인증 필수 여부

## Terminal을 이용하여 새로 추가한 앱에 대해 Migration 수행
