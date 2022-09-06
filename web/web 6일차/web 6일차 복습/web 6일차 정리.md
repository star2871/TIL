# Bootstrap 컴포넌트
## Components
### Bootstrap의 다양한 UI 요소를 활용할 수 있음
### 아래 Components 탭 및 검색으로 원하는 UI 요소를 찾을 수 있음 
### 기본 제공된 Components를 변환해서 활용
![[Components 활용 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%206%EC%9D%BC%EC%B0%A8/web%206%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/Components%20%ED%99%9C%EC%9A%A9%20%EC%98%88%EC%8B%9C.jpg)
## Bootstrap 가져오는 코드
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
	<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
	rel="stylesheet" integrity="sha384
	gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx"
	crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script
src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
  </body>
</html>
```


## Buttons
### 클릭 했을 때 어떤 동작이 일어나도록 하는 요소
```
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>

<button type="button" class="btn btn-link">Link</button>
```
![[버튼 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%206%EC%9D%BC%EC%B0%A8/web%206%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/%EB%B2%84%ED%8A%BC%20%EC%98%88%EC%8B%9C.jpg)
### `<button>`, `<a>`, `<input>` 거의 같은 역할로 사용 할수 있다.
### `<button>`은 Outline, Sizes, Disabled(비활성화 상태), Block, plugin, Toggle states(상태 변환)등 다양하게 사용 할 수 있다.

## Dropdowns
### dropdown, dropdown-menu, dropdown-item 클래스를 활용해 옵션 메뉴를 만들 수 있습니다.
```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown button
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
```
![[dropdown button.jpg]](https://github.com/star2871/TIL/blob/master/web/web%206%EC%9D%BC%EC%B0%A8/web%206%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/dropdown%20button.jpg)
### `<dropdowns>`은 `<botton>`와 함께 사용한다. Split button, Sizing, 위에 그림에서 하얀부분 배경색을 바꾸는 것, Centered, Dropup, Dropend, Dropstart, Menu items, Active, Disabled, Menu alignment,  Responsive alignment, Alignment options, Menu content(Headers, Dividers, Text, Forms), Dropdown options, Auto close behavior등이 있다.

## Forms
### form-control 클래스를 사용해 `<input>` 및 `<form>`태그를 스타일링할 수 있다.
![[form 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%206%EC%9D%BC%EC%B0%A8/web%206%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/form%20%EC%98%88%EC%8B%9C.jpg)
```html
<div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Email address</label>
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
</div>
<div class="mb-3">
  <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
  <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
</div>
```
### `<form>`은 Sizing, Disabled, Readonly, Readonly plain text, File input, Color, Datalists 등이 있다.

## Navbar
### navar 클래스를 활용하면 네비게이션 바를 제작할 수 있다.
![[Navbar 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%206%EC%9D%BC%EC%B0%A8/web%206%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/Navbar%20%EC%98%88%EC%8B%9C.jpg)
```html
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```
### `<navbar>`에는 Brand(Text, Image, Image and text), Nav, Forms, Text, Color schemes, Containers, Placement, Scrolling, Responsive behaviors(Toggler, External content, Offcanvas)등이 있다.

## Carousel
### 콘텐츠(사진)을 순환시키기 위한 슬라이드쇼
![[Carousel 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%206%EC%9D%BC%EC%B0%A8/web%206%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/Carousel%20%EC%98%88%EC%8B%9C.jpg)
```html
<div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
```
### `<Carousel>`은 Slides only, With controls, With indicators, With captions, Crossfade, Individual `.carousel-item` interval, Disable touch swiping, Dark variant, Custom transition등이 있다.

## Modal
### 사용자와 상호작용 하기 위해서 사용하며, 긴급 상황을 알리는 데 주로 사용
### 현재 열려 있는 페이지 위에 또 다른 레이어를 띄움 
### 페이지를 이동하면 자연스럽게 사라짐(제거를 하지 않고도 배경 클릭시 사라짐 – 옵션에 따라 다름)
![[Modal 예시1.jpg]](https://github.com/star2871/TIL/blob/master/web/web%206%EC%9D%BC%EC%B0%A8/web%206%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/Modal%20%EC%98%88%EC%8B%9C1.jpg)
![[Modal 예시2.jpg]](https://github.com/star2871/TIL/blob/master/web/web%206%EC%9D%BC%EC%B0%A8/web%206%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/Modal%20%EC%98%88%EC%8B%9C2.jpg)
```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```
### `<modal>`에는 Live demo, Static backdrop, Scrolling long content, Vertically centered, Tooltips and popovers, Using the grid, Varying modal content, Toggle between modals, Change animation, Remove animation, Dynamic heights, Accessibility, Embedding YouTube videos,  Optional sizes, Fullscreen Modal등이 있다.