# Event

## Event(이벤트) 개념

- ### 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
- ### 이벤트 발생
	- #### 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
	- #### 특정 메서드를 호출(Element.click())하여 프로그래밍적으로도 만들어 낼 수 있음
![[이벤트 예시.jpg]]

## Event의 역할 (1/3)
### 1. "~하면 ~한다."
### 2. “클릭하면, 경고창을 띄운다. ”
### 3. “특정 이벤트가 발생하면, 할 일(함수)을 등록한다. ”

## Event handler - addEventListener() (1/4)
- ### EventTarget.addEventListener()
	- #### 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정
	- #### 이벤트를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능

## Event handler - addEventListener() (2/4)
- ### target.addEventListener(type, listener[, options])
	- #### type
		- ##### 반응 할 이벤트 유형 (대소문자 구분 문자열)
	- #### listener
		- ##### 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체 EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함

## Event handler - addEventListener() (3/4)
### "대상에 특정 이벤트가 발생하면, 할 일을 등록하자"

## Event handler - addEventListener() (4/4)
### “대상에 특정 이벤트가 발생하면, 할 일을 등록하자”
### EventTarget.addEventListener(type, listener)

## Event 취소
- ### event.preventDefault()
- ### 현재 이벤트의 기본 동작을 중단
- ### HTML 요소의 기본 동작을 작동하지 않게 막음
	- #### ex) a 태그의 기본 동작은 클릭 시 링크로 이동 / form 태그의 기본 동작은 form 데이터 전송
- ### 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소

## alert() 함수
### `alert` 함수는 하나의 인수(argument)를 취합니다 — alert 박스에 표시될 문자열입니다. 메시지를 바꾸기 위해서 문자열에 변화를 줘 보세요
```
alert('입력한 글자가 8글자 이상이어야 합니다.');
```
![[alert 예시.jpg]]

### if문을 사용하면 글자수 제한을 걸수 있고 비밀번호 일치 불일치도 넣을수 있다.
```
<form name="join">

  비밀번호 : <input type="password" id="password1">

  비밀번호확인 : <input type="password" id="password2">

  <input type="button" onclick="test()" value="회원가입">

</form>

  

<script type="text/javascript">

  function test() {

    var p1 = document.getElementById('password1').value;

    var p2 = document.getElementById('password2').value;

    if(p1.length < 8) {

            alert('입력한 글자가 8글자 이상이어야 합니다.');

            return false;

        }

        if( p1 != p2 ) {

          alert("비밀번호가 불일치합니다.");

          return false;

        } else{

          alert("비밀번호가 일치합니다.");

          return true;

        }

  }

</script>
```
![[비밀번호 일치.jpg]]
![[비밀번호 불일치.jpg]]
![[alert 예시 1.jpg]]
