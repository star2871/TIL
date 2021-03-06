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




- 식별자

  - 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name)

  - 규칙

    - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
    - 첫 글자에 숫자가 올 수 없음
    - 길이제한이 없고, 대소문자를 구별
    - 다음의 키워(keywords)는 예약어(reseved words)로 사용할 수 없음

  - 키워드/ 예약어

    ```python
    import keyword
    print(keyword.kwlist)
    ```

    ['False', 'None', 'True', 'and', 'as', 'assert',  'async', 'await', 'break', 'class', 'continue',  'def', 'del', 'elif', 'else', 'except',  'finally', 'for', 'from', 'global', 'if',  'import', 'in', 'is', 'lambda', 'nonlocal',  'not', 'or', 'pass', 'raise', 'return', 'try',  'while', 'with', 'yield']

  - 내장함수나 모듈 등의 이름으로도 만들면 안됨

    - 기존의 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않음

      ```python
      print(5)
      print = 'hi'
      print(5)
      ```

      TypeError Traceback (most recent call last) 

      1 print(5)  

      2 print = 'hi’  

      ----> 3 print(5)  

      TypeError: 'str' object is not callable

  

  ​			내장 함수 print가 아닌 식별자(변수명)가 print인 문자열 hi로 활용됨

  

- 사용자 입력

  - input([prompt])

    - 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수

    - 대괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력할 수 있음

    - 반환값은 항상 문자열의 형태로 반환

      ``` python
      name = input('이름을 입력해주세요 : ')
      print(name)
      # 이름을 입력해주세요 : 파이썬
      type(name)
      # str
      ```

  

- 주석(Comment)

  - 코드에 대한 설명
    - 중요한 점이나 다시 확인하여야 하는 부분을 표시
    - 컴퓨터는 주석을 인식하지 않음 사용자만을 위한 것

  - 가장 중요한 습관 

    - 개발자에게 주석을 작성하는 습관은 매우 중요 

    - 쉬운 이해와 코드의 분석 및 수정이 용이 

      ✓ 주석은 코드 실행에 영향을 미치지 않을 뿐만 아니라 

      ✓ 프로그램의 속도를 느리게 하지 않으며, 용량을 늘리지 않음

  - 한 줄 주석 

    - 주석으로 처리될 내용 앞에 ‘#’ 을 입력 

    - 한 줄을 온전히 사용할 수도 있고, 그 줄 코드 뒷부분에 작성 할 수 있음

      ```python
      # 주석(comment)입니다.
      
      # print('hello')
      print('world') # 주석
      ```



- 파이썬 자료형 분류

  - 불린형(Boolean Type) 

  - 수치형(Numeric Type) 

    - int (정수, integer) 
    - float (부동소수점, 실수, floating point number) 
    - complex (복소수, complex number) 

  - 문자열(String Type) 

  -  None 

    - 파이썬 자료형 중 하나 

    - 파이썬에서는 값이 없음을 표현하기 위해 None 타입이 존재함. 

    - 일반적으로 반환 값이 없는 함수에서 사용하기도 함.

      ```python
      print(type(None))
      # <class 'NoneType'>
      a = None
      print(a)
      # None
      ```



- 불린(Boolean)

  - True / False 값을 가진 타입은 bool 

  - 비교/논리 연산을 수행함에 있어서 활용됨 

  - 다음은 모두 False로 변환 

    - 0, 0.0, (), [], {}, '', None

  - bool() 함수

    - 특정 데이터가 True인지 False인지 검증

      ```python
      bool(0)
      # False
      bool(1)
      # True
      bool(-1)
      # True
      bool('')
      # False
      bool([])
      # False
      bool([1, 2, 3])
      # True
      ```

  - 논리 연산자

    - 논리식을 판단하여 참(True)와 거짓(False)를 반환함

      | 연산자  |              내용              |
      | :-----: | :----------------------------: |
      | A and B |    A와 B 모두 True시, True     |
      | A or B  |   A와 B 모두 False시, False    |
      |   Not   | True를 False로, False를 True로 |
    
    - and : 모두 참인 경우 참, 그렇지 않으면 거짓
    
      | 논리연산자 and  | 내용  |
      | --------------- | ----- |
      | True and True   | True  |
      | True and False  | False |
      | False and True  | False |
      | False and False | False |
    
    - or : 둘 중 하나만 참이라도 참, 그렇지 않으면 거짓
    
      | 논리연산자 or   | 내용  |
      | --------------- | ----- |
      | True and True   | True  |
      | True and False  | True  |
      | False and True  | True  |
      | False and False | False |
    
    - not : 참 거짓의 반대의 결과
    
      | 논리연산자 not | 내용  |
      | -------------- | ----- |
      | not True       | False |
      | not False      | True  |
    
    - 연산자 예제
    
      ```python
      num = 100
      num >= 100 and num % 3 == 1
      # True
      ```



- 수치형(Numeric Type)

  - 정수(int)

    - 모든 정수의 타입은 int
      - Python 3부터는 long 타입은 없고, 모두 int로 표기 됨 
      - 여타 프로그래밍 언어, Python 2에서는 OS기준 32/64비트 
    - 매우 큰 수를 나타낼 때 오버플로우가 발생하지 않음 
      - 오버플로우(overflow) : 데이터 타입별로 사용할 수 있는 메모리의 크기를 넘어서는 상
      - Arbitrary precision arithmetic(임의 정밀도 산술)을 통해 고정된 형태의 메모리가 아닌 가용 메모리들을 활 용하여 모든 수 표현에 활용
    - 모든 정수의 타입은 int 
    - 오버플로우가 발생하지 않음

  - 실수(float)

    - 정수가 아닌 모든 실수는 float 타입 

    - 부동소수점 

      - 실수를 컴퓨터가 표현하는 방법 - 2진수(비트)로 숫자를 표현 
      - 이 과정에서 floating point rounding error가 발생하여, 예상치 못한 결과가 발생

    - Floatin point rounding error

      - 부동소수점에서 실수 연산 과정에서 발생 가능 

        - 값 비교하는 과정에서 정수가 아닌 실수인 경우 주의할 것

          ```python
          # 아래는 참일까? 거짓일까?
          3.14 - 3.02 == 0.12
          ```

          ```python
          3.14 - 3.02
          #0.12000000000000001
          ```

      - 부동소수점에서 실수 연산 과정에서 발생 가능 

        - 값 비교하는 과정에서 정수가 아닌 실수인 경우 주의할 것 

        - 매우 작은 수보다 작은지를 확인하거나 math 모듈 활용

          ```python
          # 1. 임의의 작은 수
          abs(a - b) <= 1e-10
          
          # 2. math 모듈 활용
          import math
          math.isclose(a, b)
          ```

  - 복소수(complex)

    - 실수부와 허수부로 구성된 복소수는 모두 complex 타입 

      - 허수부를 j로 표현

        ```python
        a = 3+4j
        type(a)
        # <classs 'complex'>
        a. real
        # 3.0
        a. imag
        # 4.0
        ```

  - 산술 연산자

    - 기본적인 사칙연산 및 수식 계산

      | 연산자 |   내용   |
      | :----: | :------: |
      |   +    |   덧셈   |
      |   -    |   뺄셈   |
      |   *    |   곱셈   |
      |   %    |  나머지  |
      |   /    |  나눗셈  |
      |   //   |    몫    |
      |   **   | 거듭제곱 |

  - 복합 연산자

    - 연산과 할당이 함께 이뤄짐

      | 연산자  |    내용    |
      | :-----: | :--------: |
      | a += b  | a = a + b  |
      | a -= b  | a = a - b  |
      | a *= b  | a = a * b  |
      | a /= b  | a = a / b  |
      | a //= b | a = a // b |
      | a %= b  | a = a % b  |
      | a **= b | a = a ** b |

  - 비교 연산자

    - 값을 비교하며, True / False  값을 리턴함

      
