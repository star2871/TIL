# Django - User model
> django.contrib.auth Documentation
## Django는 기본적으로 `django.contrib.auth` 앱을 통해 회원관리를 할 수 있는 기능을 제공하는데, `auth`의 `User model`을 통해 여러 인증을 구현할 수 있다.

## Fields
### 이 User 모델은 다음과 같은 필드들을 기본적으로 제공한다.

### 1. username
> 필수값! 150자 이하의 영숫자, _, @, +, ., -를 포함할 수 있다.
- ### `max_length`는 여러 케이스에 대해 충분해야 한다.
  - ### 만약 더 긴 길이가 필요한 경우, 사용자 정의 모델을 사용하자.

