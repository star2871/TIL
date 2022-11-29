# Models.py
## 우선 모델부터 만들어보겠습니다.

## 좋아요 기능의 경우 한명의 유저가 여러 게시물에 좋아요를 누를 수 있고, 또 하나의 게시물에 여러명의 유저가 좋아요를 누를 수 있어야겠죠? 그래서 데이터베이스 간에 다대다(N:M) 관계 설정이 필요합니다.
```
class Blodapp(models.Model): #게시물  
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
		# user model과 M:M 관계를 가지는 field 입니다.
    like = models.ManyToManyField(User, related_name='likes',blank=True)
```

## N:M 관계를 위해 ManyToManyField를 사용하였습니다.ManyToManyField 에 첫번째 인자에는 관계되는 모델을 입력합니다. 그리고 related_name 속성은, 첫번째 인자에서 접근할 때 사용하는 변수명을 의미합니다.
- ## Blogapp -> Blogapp.likes
- ## User ->  User.likes

## blank=True는 필드가 폼(입력 양식)에서 빈 채로 저장되는 것을 허용합니다. 유효성 검사와 관련있는 것으로 form.is_vaild()가 호출될 때 폼 유효성 검사에 사용되어집니다. * null =True는 DB와 관련이 있는데, 주어진 db 컬럼 값이 null(정보없음)을 가질 것인지 아닌지를 정의합니다. 이때 CharFields()와 TextFields()에서는 예외로, NULL을 저장하지 않으며, 빈 값을 빈 문자열('')로 저장합니다.

# views.py
```
from django.http import HttpResponse,JsonResponse
import json
    
def likes(request): 
    if request.is_ajax(): #ajax 방식일 때 아래 코드 실행
        blog_id = request.GET['blog_id'] #좋아요를 누른 게시물id (blog_id)가지고 오기
        post = Blogapp.objects.get(id=blog_id) 
				
        if not request.user.is_authenticated: #버튼을 누른 유저가 비로그인 유저일 때
            message = "로그인을 해주세요" #화면에 띄울 메세지 
            context = {'like_count' : post.like.count(),"message":message}
            return HttpResponse(json.dumps(context), content_type='application/json')

        user = request.user #request.user : 현재 로그인한 유저
        if post.like.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
            post.like.remove(user) #like field에 현재 유저 추가
            message = "좋아요 취소" #화면에 띄울 메세지
        else: #좋아요를 누르지 않은 유저일 때
            post.like.add(user) #like field에 현재 유저 삭제
            message = "좋아요" #화면에 띄울 메세지
        # post.like.count() : 게시물이 받은 좋아요 수  
        context = {'like_count' : post.like.count(),"message":message}
        return HttpResponse(json.dumps(context), content_type='application/json')
```
## HttpResponse는 비동기로 데이터를 가지고 오기 위해 import 해주었습니다. (render나 redirect는 새로고침하게 되는 아이들 이니까...-) 또 json을 사용할거라, 이를 만들어주었습니다.

## 우선 로그인하지 않은 유저가 좋아요를 누르려고 할 때는 '로그인을 해주세요'라는 메세지를 띄워주기 위해 message라는 변수에 담아 context 변수에 넣어줍니다. 또 count라는 함수를 이용하여 like에 몇명이 있는지 세어본 후, 이를 'like_count'라는 변수에 담아 보내줍니다.

## 이때 HttpResponse를 통해 데이터를 보낼텐데, 딕셔너리를 json 형태로 바꾸어 보내주기 위해 json.dumps를 사용해줍니다.

## 그리고 로그인한 유저가 좋아효 버튼을 누르면, 현재 로그인한 유저 정보를 가져와서 fillter함수를 이용하여 해당 값이 존재하는지 확인하고, 있으면 .remove 함수를 통해 유저 값을 제거해줍니다.

# urls.py
```
path('like/', blogapp.views.likes, name="likes"),
```

# detail.html
```
    <button id="{{blog.id}}" onclick="post_like(this.id)"> <!--좋아효 버튼을 만들어주기-->
        좋아요
        <span id="like_count">{{blog.like.count}}</span> 
        <!--{{blog.like.count}}가 없어도 되지만! 처음에 0을 보여주기 위해 넣어줌!-->
    </button>

    <!-- toast message -->
    <div class='toast' style='display:none'>
        <div id="message"></div>
    </div>    
	
    <script src="https://code.jquery.com/jquery-3.5.1.js"
        integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
    <script type="text/javascript">
        function post_like(id) {
            console.log("hi")
            $.ajax({
                url: "{%url 'likes'%}", // data를 전송할 url 입니다.
                data: {
                    'blog_id': id
                }, // post_id 라는 name으로 id 값 전송
                dataType: "json",
                success: function (response) { // ajax 통신이 정상적으로 완료되었을 때
                    $('#like_count').html(response.like_count) //id가 like_count의 내용을 전송받은 좋아요 수로 바꾼다
                    $('#message').html(response.message) //id가 message의 내용을 전송받은 message로 바꾼다
                    $('.toast').fadeIn(400).delay(100).fadeOut(400) //class가 toast인 것을 서서히 나타나게 하는 메서드입니다.
                }
            })
        }
    </script>
```
## button은 좋아요 버튼으로 이 버튼을 누르면 자동으로 like.count가 조절이 되게끔 만들어줍니다.

## `<script>` 태그는 body 태그 최하단에 위치하게 합니다.
## jquery cdn을 넣어줍니다.

## .ajax() 메서드는 jQuery가 ajax와 관련하여 제공하는 메서드로 HTTP 요청으로 서버와 통신해줍니다.

## 이때 ajax 안에 여러 옵션을 쓸 수 있습니다. 오늘은 url, data, dataType등을 넣어보겠습니다.

# 아이콘 넣기
```
<head>
	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">
</head>
<body>
 <!--중략-->
  <button id="{{blog.id}}" onclick="post_like(this.id)">
          {%if request.user in blog.like.all%}
          <!-- 로그인 한 유저가 좋아요를 누른 유저일때  -->
          <i id="heart" class="fas fa-heart"></i>
          {%else%}
          <!-- 로그인 한 유저가 좋아요를 누른 유저가 아닐 때  -->
          <i id="heart" class="far fa-heart"></i>
          {%endif%}
          <span id="like_count">{{blog.like.count}}</span>
  </button>
    <script src="https://code.jquery.com/jquery-3.5.1.js"
        integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
    <script type="text/javascript">
        function post_like(id) {
            console.log("hi")
            $.ajax({
                url: "{%url 'likes'%}", // data를 전송할 url 입니다.
                data: {
                    'blog_id': id
                }, // post_id 라는 name으로 id 값 전송
                dataType: "json",
                success: function (response) { // ajax 통신이 정상적으로 완료되었을 때
                    $('#like_count').html(response.like_count) //id가 like_count의 내용을 전송받은 좋아요 수로 바꾼다
                    $('#message').html(response.message) //id가 message의 내용을 전송받은 message로 바꾼다
                    $('.toast').fadeIn(400).delay(100).fadeOut(400)
                    if (response.message == "좋아요")
                    //좋아요 눌렀을 때 
                    {
                        $('#heart').attr("class", "fas fa-heart")
                    } else if (response.message == "좋아요 취소")
                    //좋아요 상태에서 다시 눌렀을 때 
                    {
                        $('#heart').attr("class", "far fa-heart")
                    }
                }
            })
        }
    </script>
</body>  
```

# 유저가 좋아요한 게시물 확인하기

# view.py
```
def myprofile(request,user_id):  
    user = User.objects.get(id = user_id)
    post_likes = user.likes.all()
    context={
        "post_likes":post_likes,
    }
    return render(request, 'myprofile.html',context)
```
# urls.py
```
urlpatterns = [
    '''중략'''
    path('myprofile/<int:user_id>',accounts.views.myprofile,name='myprofile'),
]
```

# templates

# myprofile.html
```
<p>내가 좋아요 누른 글</p>
{% for post in post_likes  %}
<a href="{%url 'read' post.id%}">{{post.title}}</p>
<p>{{post.content|truncatewords:50}}</p>
<p>{{post.user}}</p>
<p>{{post.updated_at|date:"Y년m월d일"}}</p>
{% endfor %}
```

# myprofile에 접근하기 위한 코드
```
<div>
    프로필<a href="{% url 'myprofile' user.id %}">{{user.username}}</a>
</div>
```
### 느낀점
### 아직은 그냥 복붙정도만 할 수 있는거 같다. 더 노력해서 자유롭게 쓰고 싶다.