# Model Form
## `form` 클래스를 상속받은 클래스 (`forms.ModelForm`)
## `form` 을 만들 때 `model` 클래스의 내역 그대로 `form`을 만든다면, (`Model Form`)
## `forms.py` 에서 `form` 필드를 중복해서 정의할 필요가 없다
## 모델과 관련된 `form` 이라면 모델 폼을 사용하는 것이 좋다

# `Form` vs `Model Form` (폼과 모델폼의 차이점)
## `Form` (일반 폼) : 직접 필드 정의, 위젯 설정이 필요
## `Model Form` (모델 폼) : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성
```
from django import forms
from .models import Post

# Form (일반 폼)
class PostForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)

# Model Form (모델 폼)
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content'] # '__all__' 설정시 전체 필드 추가
```
