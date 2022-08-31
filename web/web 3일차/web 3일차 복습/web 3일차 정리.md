# CSS position
## 1. 문서 상에서 요소의 위치를 지정
## 2. static : 모든 태그의 기본 값(기준 위치)
- ### 일반적인 요소의 배치 순서에 따름(좌측 상단)
- ### 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

![[static.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/static.jpg)

## 3. 아래는 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
### 1. relative : 상대 위치 (임시 이동, 원래 자리는 비워둬야한다.)
- 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
- 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)
![[relative.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/relative.jpg)
### 2. absolute : 절대 위치 (완전히 이동, 부모요소(static)기준으로 한다.)
- 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남) 
- static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)
![[absolute.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/absolute.jpg)
absolute 예시
![[absolute 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/absolute%20%EC%98%88%EC%8B%9C.jpg)
### 3. fixed : 고정 위치
- 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
- 부모 요소와 관계없이 viewport를 기준으로 이동
	- 스크롤 시에도 항상 같은 곳에 위치함
![[fixed.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/fixed.jpg)
fixed 예시
![[fixed 예시.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/fixed%20%EC%98%88%EC%8B%9C.jpg)
### 4. sticky : 스크롤에 따라 static -> fixed로 변경
- 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성
- 일반적으로 Navigation Bar에서 사용됨.

# CSS 원칙
## 1. CSS 원칙 I, II : Normal flow 
- 모든 요소는 네모(박스모델), 좌측상단에 배치 
- display에 따라 크기와 배치가 달라짐
## 2. CSS 원칙 III
- position으로 위치의 기준을 변경 
	- relative : 본인의 원래 위치
	- absolute : 특정 부모의 위치
	- fixed : 화면의 위치
	- sticky: 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경

# CSS layout techniques
## 1. Float
- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함 
- 요소가 Normal flow를 벗어나도록 함
![[Float 예시 1.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/Float%20%EC%98%88%EC%8B%9C.jpg)
## 2. Flexbox
### (수동 값 부여 없이) 
### 1. 수직 정렬 
### 2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치
### 3. flexbox 시작
### 부모 요소에 display: flex 혹은 inline-flex
![[flexbox 시작예시 1.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/flexbox%20%EC%8B%9C%EC%9E%91%EC%98%88%EC%8B%9C.jpg)
- 배치 설정
	- flex-direction
- 공간 나누기
	- justify-content (main axis)
- 정렬 
	- align-items (모든 아이템을 cross axis 기준으로)
### 4. flex-direction
- Main axis 기준 방향 설정 
- 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)
	- row 왼쪽에서 오른쪽
	- row-reverse 오른쪽에서 왼쪽
	- column 위에서 아래로
	- column-revers 아래에서 위로
### 5. flex-wrap
- 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
- 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함
- `wrap`은 내가 원하는 px만큼 자리를 차지하고 자리가 부족하면 밑으로 내려간다.
![[wrap 1.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/wrap.jpg)
- `norap`은 크기를 줄여서 어떻게는 그 범위에 넣는다.
![[nowrap 2.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/nowrap.jpg)
### 6. justify-content
- `flex-start`는 왼쪽 끝으로 모인다.
![[flex-start.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/flex-start.jpg)
- `flex-end`는 오른쪽 끝으로 모인다.
![[flex-end.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/flex-end.jpg)
- `center`는 가운데 모인다.
![[center.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/center.jpg)
- `space-around`는 박스 세개 각각의 공간이 있다.
![[space-around.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/space-around.jpg)
- `space-evenly`는 박스 세개 각각의 공간이 일정하다.
![[space-evenly.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/space-evenly.jpg)
### 7. align-items
- `stretch`는 컨테이너를 가득 채움
![[align-items stretch.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/align-items%20stretch.jpg)
- `flex-start`는 위로
![[align-items flex-start 1.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/align-items%20flex-start.jpg)
- `flex-end`는 아래로
![[align-items flex-end 1.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/align-items%20flex-end.jpg)
- `center`는 가운데로
![[align-items center 1.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/align-items%20center.jpg)
- `baseline`는 텍스트를 baseline에 기준선을 맞춤
![[align-items baseline.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/align-items%20baseline.jpg)
### 8. flex-grow : 남은 영역을 아이템에 분배
### 9. order : 배치순서
![[grow, order.jpg]](https://github.com/star2871/TIL/blob/master/web/web%203%EC%9D%BC%EC%B0%A8/web%203%EC%9D%BC%EC%B0%A8%20%EB%B3%B5%EC%8A%B5/%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%9E%90%EB%A3%8C/grow%2C%20order.jpg)