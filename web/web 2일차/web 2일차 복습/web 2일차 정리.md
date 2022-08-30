# CSS 기본 스타일
## 크기 단위
## 1. px (픽셀)
- 모니터 해상도의 한 화소인 '픽셀' 기준
- 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
## 2. %
- 백분율 단위
- 가변적인 레이아웃에서 자주 사용
### 3. em
- (바로 위, 부모 요소에 대한) 상속의 영향을 받음
- 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
### 4. rem
- (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
- 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
![[크기 단위.jpg]](https://github.com/star2871/TIL/blob/master/web/web%202%EC%9D%BC%EC%B0%A8/web%202%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/%ED%81%AC%EA%B8%B0%20%EB%8B%A8%EC%9C%84.jpg)
- 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (디바이스 화면)
- 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
- 예) vw, vh, vmin, vmax

## 색상 단위
### 1. 색상 키워드(background-color: red;)
- 대소문자를 구분하지 않음
- red, blue, black 과 같은 특정 색을 직접 글자로 나타냄
### 2. RGB 색상(background-color: rgb(0, 255, 0);)
- 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
- ‘#’ + 16진수 표기법
- rgb() 함수형 표기법
### 3. HSL 색상(background-color: hsl(0, 100%, 50%);)
- 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
- 색상, 채도, 명도
### 4. a는 alpah(투명도)
![[색상 단위.jpg]](https://github.com/star2871/TIL/blob/master/web/web%202%EC%9D%BC%EC%B0%A8/web%202%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/%EC%83%89%EC%83%81%20%EB%8B%A8%EC%9C%84.jpg)

## CSS 문서 표현
### 1. 텍스트
- 서체(font-family), 서체 스타일(font-style, font-weight 등)
- 자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height) 등
### 2. 컬러(color), 배경(background-image, background-color)
### 3. 기타 HTML 태그별 스타일링
- 목록(li), 표(table)

## CSS Selectors
### 선택자(Selector) 유형
#### 기본 선택자
- 전체 선택자, 요소 선택자
- 클래스 선택자, 아이디 선택자, 속성 선택자

## CSS 적용 우선순위(cascading order)
### 1. 중요도(Importance) : 사용시 주의
``*`` !important
### 2. 우선 순위(Specificity)
``*`` 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
### 3. CSS 파일 로딩 순서
```
<!--

  * : 가장 쉽다. 모든 것에 된다.

  

  요소 선택 : *보다는 덜한데..

  

  클래스 : 요소보다는 덜한데..

  

  id : 문서 하나!

  

  인라인 스타일 : 너가 굳이 그렇게 하겠다면,

  우선순위가 높은 것이길 바라...

  재사용도 못하고 완전 쓰레긴데...

  굳이굳이 그러고싶다면 우선순위 높여줄게

  

  !important : 어? 이거 썼어. 그러면 ㅇㅋ

  너의 소스코드의 핵폭탄을 투하한다면야..

  ㅇㅋ

  => 외부라이브러리에서 많이 쓰는 패턴.

  왜? 외부라이브러리 입장에서는

  내가 적용되야 이걸 쓰는 의미가 있으니까!

  

 -->
```

