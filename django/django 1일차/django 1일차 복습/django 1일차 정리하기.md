## Django

#### Framework = Frame(뼈대) + work(일하다)
- 서비스 개발에 필요한 기능들을 미리 구현해서 모아놓은 것

#### 클라이언트와 서버
* 오늘날 우리가 사용하는 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작
* 클라이언트에서 요청을 하면 서버에서 요청을 받고 응답을 하는 구조로 상호작용함
* 이 중에서 Django는 서버를 구현하는 웹 프레임워크 


#### 클라이언트
* 웹 사용자의 인터넷에 연결된 장치
* Chrome 또는 Firefox 와 같은 웹 브라우저
* 서비스를 요청하는 주체


#### 서버
* 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
* 클라이언트가 웹 페이지에 접근하려고 할 때 클라이언트 서버로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 포시됨
* 요청에 대해 서비스를 응답하는 주체


## Web browser와 Web page

#### 동적 웹 페이지
* Dynamic Web page
* 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
* 웹 페이지의 내용을 바꿔주는 주체 == 서버
  * 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
  * 사용자의 요청을 받아서 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크가 Django

#### 정적 웹 페이지
-   Static Web page
-   있는 그대로를 제공하는 것(served as-is)
-   HTML 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 것

### Git Bash에서 웹 서버 구축

Git Bash에서 처음 `~` 표시는 `/c/Users/user` 위치를 의미한다

1.  처음 확인사항
```
$ python --version  # 파이썬 설치되어있는지 확인
$ mkdir server  # 폴더 생성
```

2.  가상환경 실행
```
$ cd server  # 폴더로 이동
$ python -m venv server-venv  # 가상환경 생성
$ ls  # 가상환경 이름 확인
server-venv/
$ source server-venv/Scripts/activate  # 가상환경 실행, 실행하면 (이름) 나타남
```

```
(server-venv)
user@DESKTOP MINGW64 ~/server
```

3.  Django 설치 & 서버 구동
```
$ pip install django==3.2.13  # 현재 가장 안정적인 django 버전(3.2.13) 설치
$ pip list  # 설치된 것들 확인
$ django-admin startproject firstpjt .  # 프로젝트 시작 명령 [프로젝트이름] [시작할경로]
$ ls  # 프로젝트 확인
firstpjt/  manage.py*  server-venv/
$ python manage.py runserver  # 서버 구동
```

4. 이후
```
Ctrl + c  # server 종료하기
$ deactivate  # 가상환경 끄기
$ code .  # vscode로 열기 
```