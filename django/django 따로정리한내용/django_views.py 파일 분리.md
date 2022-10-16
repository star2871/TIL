# 장고에 기능을 계속 추가하다보면 뷰 파일(views.py)에 함수가 계속 늘어나 불편함을 느끼게 될 것이다. 현재 파이보에 추가된 기능만으로도 뷰 파일이 매우 방대해졌다.뷰 파일에 함수가 많아지면 관리하기 힘들어지기 때문에 이쯤에서 뭔가 개선이 필요함을 느끼게 된다. 여기서는 두 가지 방법에 대해서 알아볼 것이다. 파이보는 결론적으로 두 번째 방법을 사용할 것이다. 하지만 두 번째 방법을 진행하기 위해서는 첫 번째 방법을 적용한 후에 가능하므로 첫 번째 방법부터 차례대로 따라해 보자.

## 첫 번째 방법
### 첫 번째 방법은 views.py 파일만 여러 파일로 분리하고 나머지는 고치지 않아도 되는 변화가 적은 방법이다.

#### base_views.py
#### question_views.py
#### answer_views.py

## 두 번째 방법
### 하지만 첫 번째 방법에는 단점이 있다. 장고는 디버깅시 보통 urls.py 파일에서 URL에 매핑된 함수를 찾는것으로 시작한다. 하지만 첫번째 방법을 사용하면 urls.py 파일에 매핑된 함수명은 알수 있지만 어떤 뷰 파일의 함수인지는 알 수가 없다. 이는 views 디렉터리의 모든 뷰 파일을 찾아봐야 하는 불편함을 초래하게 한다. 이러한 이유로 혼자가 아닌 여러명이 함께 하는 프로젝트라면 첫번째 방법은 절대로 추천하지 않는다. 두번째 방법은 views 디렉터리의 __init__.py 파일을 제거하고 pybo/urls.py에서 views.index 대신 base_views.index 와 같이 전체 경로를 써주는 방법이다.

```
from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'pybo'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:question_id>/',
         base_views.detail, name='detail'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
]
```