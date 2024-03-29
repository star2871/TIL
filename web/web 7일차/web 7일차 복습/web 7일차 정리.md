# Bootstrap Grid System

## Grid system (web design)
### 요소들의 디자인과 배치에 도움을 주는 시스템 
### 기본 요소
- Column : 실제 컨텐츠를 포함하는 부분 
- Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격) 
- Container : Column들을 담고 있는 공간
![[grid 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%207%EC%9D%BC%EC%B0%A8/web%207%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/grid%20%EC%98%88%EC%8B%9C.jpg)

## Bootstrap Grid system은 flexbox로 제작됨
## container, rows, column으로 컨텐츠를 배치하고 정렬
## 반드시 기억해야 할 2가지 !
- 12개의 column(중요)
- 6개의 grid breakpoints
```
<div class="container">
	<div class="row">
		<div class="col"></div>
		<div class="col"></div>
		<div class="col"></div>
	</div>
</div>
```

## Grid system breakpoints
![[grid system breakpoints.jpg]](https://github.com/star2871/TIL/blob/master/web/web%207%EC%9D%BC%EC%B0%A8/web%207%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/grid%20system%20breakpoints.jpg)

## Grid system breakpoints 연습하기

### grid 1 예시
```
<div class="container">
	<h2 class="text-center">column</h2>
	<div class="row">
		<div class="col">1</div>
		<div class="col">2</div>
		<div class="col">3</div>
	</div>
</div>

```
![[gird 그림 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%207%EC%9D%BC%EC%B0%A8/web%207%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/gird%20%EA%B7%B8%EB%A6%BC%20%EC%98%88%EC%8B%9C.jpg)

### grid 2 예시
```
<div class="row">

  <div class="box col-3">1</div>

  <div class="box col-6">2</div>

  <div class="box col-3">3</div>

</div>

<hr>

<div class="row">

  <div class="box col-1">1</div>

  <div class="box col-1">2</div>

  <div class="box col-1">3</div>

  <div class="box col-1">4</div>

  <div class="box col-1">5</div>

  <div class="box col-1">6</div>

  <div class="box col-1">7</div>

  <div class="box col-1">8</div>

  <div class="box col-1">9</div>

  <div class="box col-1">10</div>

  <div class="box col-1">11</div>

  <div class="box col-1">12</div>

  <div class="box col-1">13</div>

</div>
```
![[gird 그림2 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%207%EC%9D%BC%EC%B0%A8/web%207%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/gird%20%EA%B7%B8%EB%A6%BC2%20%EC%98%88%EC%8B%9C.jpg)

## grid 3 예시
```
<div class="row">

  <div class="box col-9">col-9</div>

  <div class="box col-4">col-4</div>

  <div class="box col-3">col-3</div>

  </div>

<hr>
```
![[grid 그림3 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%207%EC%9D%BC%EC%B0%A8/web%207%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/grid%20%EA%B7%B8%EB%A6%BC3%20%EC%98%88%EC%8B%9C.jpg)

## grid 4 예시
```
<h2 class="text-center">Grid breakpoints</h2>

<div class="row">

  <div class="box col-sm-8 col-md-4 col-lg-5">1</div>

  <div class="box col-8 col-sm-2 col-md-4 col-lg-2">2</div>

  <div class="box col-2 col-sm-2 col-md-4 col-lg-5">3</div>

</div>

<hr>

  

<h2 class="text-center">nesting</h2>

<div class="row">

  <div class="box col-6">

    <div class="row">

      <div class="box col-3">1</div>

      <div class="box col-3">2</div>

      <div class="box col-3">3</div>

      <div class="box col-3">4</div>

    </div>

  </div>

  <div class="box col-6">1</div>

  <div class="box col-6">2</div>

  <div class="box col-6">3</div>

</div>

<hr>

  

<h2 class="text-center">offset</h2>

<div class="row">

  <div class="box col-md-4 offset-4">.col-md-4 .offset-4</div>

  <div class="box col-md-4 offset-md-4 offset-lg-2">.col-md-4 .offset-md-4 .offset-lg-2</div>

</div>

<hr>
```
![[grid 그림4 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%207%EC%9D%BC%EC%B0%A8/web%207%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/grid%20%EA%B7%B8%EB%A6%BC4%20%EC%98%88%EC%8B%9C.jpg)

## grid 5 예시
```
<h2 class="text-center">alignment</h2>

<div class="row parent justify-content-center align-items-center">

  <div class="box col-4 justify-content-center / align-items-center"></div>

</div>

<hr>
```

![[grid 그림5 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%207%EC%9D%BC%EC%B0%A8/web%207%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/grid%20%EA%B7%B8%EB%A6%BC5%20%EC%98%88%EC%8B%9C.jpg)

## grid 6 예시
```
<div class="row parent">

  <div class="box col-4 align-self-start">1</div>

  <div class="box col-4 align-self-center">2</div>

  <div class="box col-4 align-self-end">3</div>

</div>
```
![[grid 그림6 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%207%EC%9D%BC%EC%B0%A8/web%207%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/grid%20%EA%B7%B8%EB%A6%BC6%20%EC%98%88%EC%8B%9C.jpg)

## @media 코드
```
@media (min-width: 576px) {

.container-sm, .container {

max-width: 540px;

  }

}

@media (min-width: 768px) {

.container-md, .container-sm, .container {

max-width: 720px;

  }

}

@media (min-width: 992px) {

.container-lg, .container-md, .container-sm, .container {

max-width: 960px;

  }

}

@media (min-width: 1200px) {

.container-xl, .container-lg, .container-md, .container-sm, .container {

max-width: 1140px;

  }

}

@media (min-width: 1400px) {

.container-xxl, .container-xl, .container-lg, .container-md, .container-sm, .container {

max-width: 1320px;

  }

}
```