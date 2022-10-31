# Django - User model
> django.contrib.auth Documentation
## Django는 기본적으로 `django.contrib.auth` 앱을 통해 회원관리를 할 수 있는 기능을 제공하는데, `auth`의 `User model`을 통해 여러 인증을 구현할 수 있다.

## Fields
### 이 User 모델은 다음과 같은 필드들을 기본적으로 제공한다.

### 1. username
> 필수값! 150자 이하의 영숫자, _, @, +, ., -를 포함할 수 있다.
- ### `max_length`는 여러 케이스에 대해 충분해야 한다.
  - ### 만약 더 긴 길이가 필요한 경우, 사용자 정의 모델을 사용하자.

### 2. first_name
> 선택값(`blank=True`). 150자 이하

### 3. last_name
> 선택값(`blank=True`). 150자 이하

### 4. email
> 선택값(`blank=True`). 이메일 주소

### 5. password
> 필수값! password에 대한 해시값과 메타데이터값
- ### Django는 원래 암호를 그대로 저장하지 않는다.

### 6. groups
> 그룹에 대한 필드

### 7. user_permissions
> 유저의 권한을 설정하는 필드

### 8. is_staff
> Boolean 타입. 이 사용자가 관리자 사이트에 접근할 수 있는지 지정한다.
- ### `True`이면 접근 가능

### 9. is_active
> Boolean 타입. 이 사용자 계정을 활성으로 간주할지를 지정한다.
- ### 계정을 삭제하는 대신, 이 flag를 `False` 지정하는 것을 권장한다.

### 10. is_superuser
> Boolean 타입. 이 사용자에게 명시적으로 할당하지 않고, 모든 권한이 있음을 지정한다.

### 11. last_login
> 사용자의 마지막 로그인 날짜/시간 (`datetime`)

### 12. date_joined
> 계정이 만들어진 날짜/시간 (`datetime`)
- ### 계정 생성 시 기본적으로 현재 날짜/시간으로 설정된다.

## Django Custom User Model 만드는 방법
> Django가 제공하는 방법

> - Proxy Model
> - User Model과 One-To-One 연결
> - AbstractBaseUser
> - AbstractUser

### 등의 방법이 있는데, 나는 이 중에서 `AbstractUser`를 이용한 방법을 사용하려고 한다!

## AbstractUser
> django의 기본 User 모델의 동작은 그대로 하고, 필드만 재정의할 때 사용하는 방식!
### 사용 방법은 간단하다.

### 1. settings.py
```
AUTH_USER_MODEL = 'account.User'	# [app].[모델명]
```
### 먼저 `AbstractUser`를 사용하기 위해 `settings.py`에 코드를 추가해준다.

### 2. models.py
```
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 기본적으로 제공하는 필드 외에 원하는 필드를 적어준다.
    nickname = models.CharField(max_length=50)
    phone = models.PhoneNumberField(unique = True, null = False, blank = False
```
### 이렇게 `AbstractUser`를 import하여 `User`가 `AbstractUser`를 상속받도록 해준다. 그 다음 원하는 필드를 적어주면 된다!
> ✋🏻 잠깐!!!
`AUTH_USER_MODEL`을 지정하기 전에 `manage.py migrate`는 절대!! 금지!!

### 3. admin.py
### 마지막으로 `admin.py`에 app 모델도 등록해주자
```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```