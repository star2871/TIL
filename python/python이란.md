# 파이썬

### 1. 기초문법

- 코드 스타일 가이드

  ```python
  print('hello')
  print('world')
  
  a = 'apple'
  
  if True:
      print(True)
  else:
      print(False)
      
  b = 'banana'
  ```



- 들여쓰기
  - Space Sensitive
    - 문장을 구분할 때, 들여쓰기를 사용
    - 들여쓰기를 할때는 4칸(space키 4번) 혹은 1탭(Tab키 1번)을 입력
      - 주의! 한 코드 안에서느 반드시 한 종류의 들여쓰기를 사용 ➡️혼용하면 안됨
        - Tab으로 들여쓰면 계속 탭으로 들여써야 한다.
        - 원칙적으로는 공백 (빈칸, space) 사용을 권장*PEP8 권장사항



- 변수 

  - 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름 

  - 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것 

    → 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음 

  - 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에, 

    즉, 참조하는 객체가 바뀔 수 있기 때문에 ‘변수’ 라고 불림

  - 변수는 할당 연산자(=)를 통해 값을 할당(assignment) 

  -  type()

    - 변수에 할당된 값의 타입 

  - id() 

    - 변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소

      ```python
      x = 'hi'
      type(x)
      # str
      id(x)
      # 4645387184
      ```

      

- 변수 연산

  ```python
  i = 5
  j = 3
  s = '파이썬'
  ```

  ```python
  # 1
  i + j = 8
  # 2
  i - j = 2
  # 3
  j = -2
  i * j = -10
  ```

  ```python
  # 1
  '안녕' + s = 안녕파이썬
  # 2
  s * 3 = '파이썬 파이썬 파이썬'
  # 3
  s = 'Python'
  s + ' is fun' = 'Python is fun'
  ```

  

- 변수 할당

  - 같은 값을 동시에 할당할 수 있음

    ```python
    x = y = 1004
    print(x, y)
    ```

  - 다른 값을 동시에 할당 할수 있음

    ```python
    x, y = 1, 2
    print(x, y)
    ```

  

- 예제

  - x = 10 y = 20 일 때,

    각각 값을 바꿔서 저장하는 코드를 작성하시오.

    방법 1 : 임시 변수 활용

    ``` python
    tmp = x
    x = y
    y = tmp
    print(x, y)
    ```

    방법 2 : Pythonic

    ```python
    y, x = x, y
    print(x, y)
    ```

    

  

  