# HTML 문서 구조화
## table의 각 영역을 명시하기 위해`<thead>` `<tbody>` `<tfoot>` 요소를 활용
![[table 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/table%20%EC%98%88%EC%8B%9C.jpg)

## `<tr>`으로 가로 줄을 구성하고 내부에는 `<th>` 혹은 `<td>`로 셀을 구성
![[tr 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/tr%20%EC%98%88%EC%8B%9C.jpg)

## colspan, rowspan 속성을 활요하여 셀 병합
![[colspan 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/colspan%20%EC%98%88%EC%8B%9C.jpg)

## `<caption>`을 통해 표 설명 또는 제목을 나타냄
![[caption 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/caption%20%EC%98%88%EC%8B%9C.jpg)

## table 태그 기본 구성
### thead
	- tr > th
### tbody
	- tr > td
### tfoot
	- tr > td
### caption
```
<body>

  <table>

    <thead>

      <tr>

        <th>ID</th>

        <th>Name</th>

        <th>Major</th>

      </tr>

    </thead>

    <tbody>

      <tr>

        <td>1</td>

        <td>홍길동</td>

        <td>Computer Science</td>

      </tr>

      <tr>

        <td>2</td>

        <td>김철수</td>

        <td>Business</td>

      </tr>

    </tbody>

    <tfoot>

      <tr>

        <td>총계</td>

        <td colspan="2">2명</td>

      </tr>

    </tfoot>

    <caption>1반 학생 명단</caption>

  </table>

</body>
```

# form
## `<form>`은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
## `<form>` 기본 속성
### action : form 을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
### methond : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
### enctype : method가 post인 경우 데이터의 유형
- application/x-www-form-urlencoded : 기본값
- multipart/form-data : 파일 전송시 (input type이 file인 경우)
```
<form action="/search" method="GET">

</form>
```

# input
### 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
### `<input>` 대표적인 속성
- name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
- value : form control에 적용되는 값 (이름/값 페어로 전송됨)
- required, readonly, autofocus, autocomplete, disabled 등
```
<form action="/search" method="GET">
<input type="text" name="q">
</form>
```
![[q=HTML 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/q%3DHTML%20%EC%98%88%EC%8B%9C.jpg)
```
<form action="/search" method="GET">
<input type="text" name="q">
</form>
```

# input label
## label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
- 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음
- label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인 할 수 있도록 함
## `<input>`에 id 속성을, 에는 for 속성을 활용하여 상호 연관을 시킴
```
<label for="agreement">개인정보 수집에 동의합니다.</label>
<input type = "checkbox" name="agreement" id="agreement">
```

# vscode에서 직접해보기
```
<body>

  <h1>Form 활용 실습</h1>

    <form action="">

      <!-- autofocus 및 label 확인 -->

      <div>

        <label for=""></label>

      </div>

      <input type="text" name="username" id="username" autofocus>

  

      <!-- disabled 및 value 확인 -->

      <div class="input-group">

        <label for="name">이름</label>

      </div>

      <input type="text" name="name" value="홍길동" id="name" disabled>

      <!-- label 확인 -->

      <div class="input-group">

        <label for="agreement">개인정보 수집에 동의합니다.</label>

      </div>

      <input type="checkbox" name="agreement" id="agreement">

      <div class="input-group">

        <label>최종 제출을 확인합니다.</label>

      </div>

      <input type="checkbox">

    </form>

    <input type="submit" value="제출">

</body>
```
![[vscode 직접작성예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/vscode%20%EC%A7%81%EC%A0%91%EC%9E%91%EC%84%B1%EC%98%88%EC%8B%9C.jpg)

# input 유형-일반
## 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
### text : 일반 텍스트 입력 
### password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
### email : 이메일 형식이 아닌 경우 form 제출 불가
### number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
### file : accept 속성을 활용하여 파일 타입 지정 가능
![[input 유형 일반 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/input%20%EC%9C%A0%ED%98%95%20%EC%9D%BC%EB%B0%98%20%EC%98%88%EC%8B%9C.jpg)

# input 유형 – 항목 중 선택
## 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
## 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
### checkbox : 다중 선택
### radio : 단일 선택
```
    <div>

      <p>checkbox</p>

      <input id="html" type="checkbox" name="language" value="html">

      <label for="html">HTML</label>

      <input id="python" type="checkbox" name="language" value="python">

      <label for="python">파이썬</label>

      <input id="python" type="checkbox" name="language" value="java">

      <label for="java">자바</label>

      <hr>

    </div>
```
![[input 유형 항목 중 선택.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/input%20%EC%9C%A0%ED%98%95%20%ED%95%AD%EB%AA%A9%20%EC%A4%91%20%EC%84%A0%ED%83%9D.jpg)

# input 유형-기타
## 다양한 종류의 input을 위한 picker를 제공
### color : color picker
### date : date picker
## hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
### hidden : 사용자에게 보이지 않는 input
![[input 유형 기타 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/input%20%EC%9C%A0%ED%98%95%20%EA%B8%B0%ED%83%80%20%EC%98%88%EC%8B%9C.jpg)

# Bootstrap
## Build fast, responsive sites with Bootstrap. 
## `Quickly` design and customize `responsive` mobile-first sites with Bootstrap, `the world’s most popular` front-end open source toolkit, featuring Sass variables and mixins, `responsive grid system`, extensive `prebuilt components`, and powerful JavaScript plugins.

# CDN
## Content Delivery(Distribution) Network
### 컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템.
#### 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점) 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐
![[CDN CSS JS 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/CDN%20CSS%20JS%20%EC%98%88%EC%8B%9C.jpg)

# spacing (margin and padding)
![[spacing 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/spacing%20%EC%98%88%EC%8B%9C.jpg)
```
<div class="mt-3 ms-5">bootstrap-spacing</div>
```

## Where property is one of:
- `m` - for classes that set `margin`
- `p` - for classes that set `padding`

## Where sides is one of:
![[spacing sides 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/spacing%20sides%20%EC%98%88%EC%8B%9C.jpg)
## Where size is one of:
![[spacing size 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/spacing%20size%20%EC%98%88%EC%8B%9C.jpg)
![[spacing size 크기 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/spacing%20size%20%ED%81%AC%EA%B8%B0%20%EC%98%88%EC%8B%9C.jpg)

## .mx-0
### 가로(왼쪽, 오른쪽) margin이 0
## .mx-auto
### 블록 요소 수평 중앙 정렬 가로 가운데 정렬!
## .py-0
### 위 아래 padding이 0

## spacing 종합
![[spacing 종합 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/spacing%20%EC%A2%85%ED%95%A9%20%EC%98%88%EC%8B%9C.jpg)
## Color
![[color 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/color%20%EC%98%88%EC%8B%9C.jpg)

## Text
![[text 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/text%20%EC%98%88%EC%8B%9C.jpg)

## Display
![[display 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/display%20%EC%98%88%EC%8B%9C.jpg)


## Position
![[position 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%205%EC%9D%BC%EC%B0%A8/web%205%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%ED%8C%8C%EC%9D%BC/position%20%EC%98%88%EC%8B%9C.jpg)
