# HTML
## 1. HTML 은 웹 콘텐츠의 의미와 구조를 정의할 때 사용합니다. 그 이외의 다른 기술은 일반적으로 웹 페이지의 모양/표현은 CSS로 하고 기능/동작은 JST로 사용한다.
## 2. HTML이란 Hyper Text Markup Language
## 3. Hyper Text란 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트이고 Markup Language란 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어이다.
## 4. HTML 기본구조
- html : 문서의 최상위(root) 요소
- body : 문서 본문 요소
	- 실제 화면 구성과 관련된 내용
예제
```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>

</body>
</html>
```
- head : 문서 메타데이터 요소
	- 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
	- 일반적으로 브라우저에 나타나지 않는 내용
## 5. HTML은 웹 브라우저에 표시되는 글과 이미지 등의 다양한 콘텐츠를 표시하기 위해 "마크업"을 사용한다. HTML 마크업은 다양한 "요소"를 사용한다. 요소 목록들은 시작할때는 `<요소>` 로 시작하고 끝날때는 `</요소>` 로 끝난다.
예시
(여는/시작)태그                       (닫는/종료)태그
# `<h1>` contents `</h1>`
## 6. 요소는 중첩될 수 있다.
	- 요소의 중첩을 통해 하나의 문서를 구조화
	- 여는 태그와 닫는 태그의 쌍을 잘 확인 해야한다.
		- 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 진다.
## 7. 요소목록
### `<head>`
- 기계가 식별할 수 있는 문서 정보(메타데이터)를 담습니다. 정보로는 문서가 사용할 제목, 스크립트, 스타일 시트 등이 있습니다.
- 예제
```
<!doctype html>
<html>
  <head>
    <title>문서 제목</title>
  </head>
</html>
```
예시
- `<title>` : 브라우저 상단 타이틀
• `<meta>` : 문서 레벨 메타데이터 요소
- `<link>` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
- `<script>` : 스크립트 요소 (JavaScript 파일/코드)
- `<style>` : CSS 직접 작성
### `<title>`
- 브라우저의 제목 표시줄이나 페이지 탭에 보이는 문서 제목을 정의합니다. 텍스트만 포함할 수 있으며 태그를 포함하더라도 무시합니다.

예제
```
<title>Grandma's Heavy Metal Festival Journal</title>
```

### `<body>`
- 보통 HTML에서 하기보다는 CSS에서 사용하는게 적합하다

### `<header>`
- 소개 및 탐색에 도움을 주는 콘텐츠를 나타낸다. 제목, 로고, 검색 폼, 작성자 이름 등의 요소도 포함할 수 있다.
- 구획 콘텐츠가 아니므로 개요에 구획을 생성하지 않는다. 대신 주위 구획의 제목(`<h1>`-`<h6>`요소)을 감싸기 위한 요소지만, 필수 사항은 아니다.
예제
```
<header>
  <h1>Main Page Title</h1>
  <img src="mdn-logo-sm.png" alt="MDN logo">
</header>

```
### `<footer>`
- 가장 가까운 구획 콘텐츠나 구획 루트의 푸터를 나타낸다. 푸터는 일반적으로 구획의 작성자, 저작권 정보, 관련 문서 등의 내용을 담는다.
사용 방법
- `<address>` 요소로 감싼 작성자 정보를 `<footer>` 요소에 배치한다.
예제
```
<footer>
  Some copyright info or perhaps some author
  info for an &lt;article&gt;?
</footer>
```
### `<article>`
- 문서, 페이지, 애플리케이션, 또는 사이트 안에서 독립적으로 구분해 배포하거나 재사용할 수 있는 구획을 나타낸다. 사용 예제로 게시판과 블로그 글, 매거진이나 뉴스 기사 등이 있다.
사용 방법
- 주로 제목(`<h1>`,`<h6>`) 요소를 `<article>`의 자식으로 포함하는 방법을 사용한다. 예를 들어 블로그 글의 댓글은, 글을 나타내는 `<article>` 요소 안에 중첩한 `<article>`로 나타낼 수 있다.
- `<article>` 요소가 중첩되어 있을 때, 
### `<section>`
- HTML 문서의 독립적인 구획을 나타내며, 더 적합한 의미를 가진 요소가 없을 때 사용합니다. 보통 `<section>`은 제목을 포함하지만, 항상 그런 것은 아닙니다.
사용 방법
- 각각의 `<section>`을 식별할 수단이 필요하다. 주로 제목(`<h1>`-`<h6>`) 요소를 `<section>`의 자식으로 포함하는 방법을 사용한다.
- 요소의 콘텐츠를 따로 구분해야 할 필요가 있으면 `<article>` 요소를 고려하라.
- `<section>` 요소를 일반 컨테이너로 사용하지 말아라. 특히 단순한 스타일링이 목적이라면 `<div` 요소를 사용해야 합니다. 대개, 문서 요약에 해당 구획이 논리적으로 나타나야 하면 `<section>`이 좋은 선택이다.
예제

이전
```
<div>
  <h2>Heading</h2>
  <img>some image</img>
</div>
```

이후
```
<section>
  <h2>Heading</h2>
  <img>some image</img>
</section>
```
### `<p>`
- 하나의 문단을 나타냅니다.  문단은 블록 레벨 요소이며, 자신의 닫는 태그(`</p>`) 이전에 다른 블록 레벨 태그가 분석되면 자동으로 닫힙니다.
### `<div>`
- 플로우 콘텐츠를 위한 통용 컨테이너입니다. CSS로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않습니다.
- 간단한 예제
```
<div>
   <p>어떤 콘텐츠든 좋습니다.
   &lt;p&gt;, &lt;table&gt;같이 말이죠. 써보세요!</p>
</div>
```

결과

어떤 콘텐츠든 좋습니다. `<p>`, `<table>`같이 말이죠. 써보세요!

### `<span>`
- 본질적으로는 아무것도 나타내지 않습니다. 스타일를 적용하기 위해서, 또는 lang 등 어떤 특성의 값을 서로 공유하는 요소를 묶을 때 사용할 수 있다. 
`<span>`과 `<div>`는 매우 유사하다. `<idv>`는 블록 레벨 요소인 반면 `<span>` 인라인 요소 입니다.
- 예제 1

HTML
```
<p><span>Some text</span></p>
```
결과
Some text
- 예제2

HTML
```
<li><span>
    <a href="portfolio.html" target="_blank">See my portfolio</a>
</span></li>
```
CSS
```
li span {
  background: gold;
 }
```
결과
[See my portfolio](https://yari-demos.prod.mdn.mozit.cloud/ko/docs/Web/HTML/Element/span/portfolio.html)








### `<img>`
- 문서에 이미지를 넣습니다.
예제
```
<img class="fit-picture"
     src="/media/cc0-images/grapefruit-slice-332-332.jpg"
     alt="Grapefruit slice atop a pile of other slices">
```
위의 예제를 통해 `<img>` 요소의 사용법을 알 수 있습니다.

-   `src` 특성은 **필수**이며, 포함하고자 하는 이미지로의 경로를 지정합니다.
-   `alt` 특성은 이미지의 텍스트 설명이며 필수는 아니지만, 스크린 리더가 `alt`의 값을 읽어 사용자에게 이미지를 설명하므로, 접근성 차원에서 **매우 유용**하다. 또한 네트워크 오류, 콘텐츠 차단, 죽은 링크 등 이미지를 표시할 수 없는 경우에도 이 속성의 값을 대신 보여준다.







### `<aside>`
- 문서의 주요 내용과 간접적으로만 연관된 부분을 나타낸다. 주로 사이드바 혹은 콜아웃 박스로 표현한다.
사용 방법
- 괄호에 묶인 텍스트라도 문서의 주요 플로우에 포함되어야 하므로 `<aside>`로 나타내선 안된다.
예제
 `<aside>` 사용하기
다음 예제는 글 내의 문단을 `<aside>`로 표시한다. 해당 문단은 글의 주제와 간접적으로만 연결되어 있다.
```
<article>
  <p>
    디즈니 만화영화 <em>인어 공주</em>는
    1989년 처음 개봉했습니다.
  </p>
  <aside>
    인어 공주는 첫 개봉 당시 8700만불의 흥행을 기록했습니다.
  </aside>
  <p>
    영화에 대한 정보...
  </p>
</article>
```

결과
디즈니 만화영화 _인어 공주_는 1989년 처음 개봉했습니다.

인어 공주는 첫 개봉 당시 8700만불의 흥행을 기록했습니다.

영화에 대한 정보...






### `<audio>`
- 문서에 소리 콘텐츠를 포함할 때 사용한다.  `src` 특성 또는 `<source>`__(en- US) 요소를 사용해 한 개 이상의 오디오 소스를 지정할 수 있으며, 다수를 지정한 경우 가장 적절한 소스를 브라우저가 고른다. MediaStream_(en-US)을 사용하면 미디어 스트림을 바라볼 수도 있다.
### `<canvas>`
- 캔버스 스크립팅 API 또는 WebGL API와 함께 사용해 그래픽과 애니메이션을 그릴 수 있다.
### `<pre>`
- 미리 서식을 지정한 텍스트를 나타내며, HTML에 작성한 내용 그대로 표현합니다. 텍스트는 보통 고정폭 글꼴을 사용해 렌더링하고, 요소 내 공백문자를 그대로 유지합니다.
-예제

HTML
```
<p>CSS로 글자 색을 바꾸는건 쉽습니다.</p>
<pre>
body {
  color:red;
}
</pre>

```

결과
```
CSS로 글자 색을 바꾸는건 쉽습니다.

body {
  color:red;
}
```
## 8. 속성(attribute)
![[속성에서 속성명과 속성값.jpg]](https://github.com/star2871/TIL/blob/master/web/web%201%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/%EC%86%8D%EC%84%B1%EC%97%90%EC%84%9C%20%EC%86%8D%EC%84%B1%EB%AA%85%EA%B3%BC%20%EC%86%8D%EC%84%B1%EA%B0%92.jpg)
- 속성 작성 방식 통일하기
	- 공백은 No!, "(쌍따움표)사용
- 속성을 통해 태그의 부가적인 정보를 설정할 수 있다. 
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공 한다. 
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재 한다.
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있다.

- HTML Global Attribute
	- id : 문서 전체에서 유일한 고유 식별자 지정 
	- class : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근) 
	- data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용 
	• style : inline 스타일 
	• title : 요소에 대한 추가 정보 지정 
	• tabindex : 요소의 탭 순서

- HTML 코드 예시
![[HTML 코드 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%201%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/HTML%20%EC%BD%94%EB%93%9C%20%EC%98%88%EC%8B%9C.jpg)

## 9. 렌더링(Rendering)
- 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정

## 10. DOM(Document Object Model) 트리
- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
	- HTML 문서에 대한 모델을 구성함
	- HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함

## 11. 인라인/ 블록요소
- HTML 요소는 크게 인라인 / 블록 요소로 나눔 
- 인라인 요소는 글자처럼 취급 
- 블록 요소는 한 줄 모두 사용

## 12. 텍스트 요소
![[텍스트 요소.jpg]](https://github.com/star2871/TIL/blob/master/web/web%201%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/%ED%85%8D%EC%8A%A4%ED%8A%B8%20%EC%9A%94%EC%86%8C.jpg)
## 13. 그룹 컨텐츠
![[그룹컨텐츠.jpg]](https://github.com/star2871/TIL/blob/master/web/web%201%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/%EA%B7%B8%EB%A3%B9%EC%BB%A8%ED%85%90%EC%B8%A0.jpg)
