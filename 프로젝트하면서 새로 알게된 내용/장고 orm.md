# 1. ORM이란?
## ORM(Object-Relational Mapping)이란 객체와 관계형 DB를 매핑해주는 것을 말합니다.즉 내가 선언한 장고 모델 (예: Board) 객체와 DB의 테이블(예: board )을 매핑해주는 것입니다. DB내 CRUD를 하기위해서는 SQL문을 사용해 직접 Create,Read,Update,Delete 하는 것이 일반적입니다. 그러나 데이터 CRUD 시 일일히 SQL문을 작성하게 되면 코드가 복잡해집니다. 이러한 문제점을 개선하고 코드를 편리하게 사용하기 위해 ORM 을 활용하고 있습니다. 추가적으로 코드 재사용으로 인한 효율성 향상 및 에러에 대한 핸들링이 가능하다는 장점덕분에 ORM을 사용합니다. 그러나 여러 테이블을 사용해 조인하는 경우 ORM 보다 실제 SQL 쿼리를 사용하는 것이 훨씬 효과적일 거라 예상합니다.

# 2. 장고(django)의 DB CRUD
## 1) 데이터 추가
- ## objects.create()
  - ### Board 객체의 필드에 title = "제목" , description = "내용" 이라는 데이터를 넣어 DB 테이블 데이터 행을 추가합니다.
> ### title = "제목" description = "내용" data = Board.objects.create(title = title, description = description)

## 2) 데이터 조회
- ## objects.all()
  - ### DB 테이블의 모든 데이터를 가져오고 싶은 경우 objects.all() 메서드를 사용합니다.
> ### boards = Board.objects.all()

## 3) 데이터 검색
- ## objects.get()
  - ### 검색 결과와 일치하는 하나의 데이터만을 반환합니다.
  - ### 파라미터와 일치하는 테이블 데이터(원하는 검색 결과)를 가져오고 싶은 경우 objects.get() 메서드를 사용합니다.
  - ### get은 객체를 반환, filter는 쿼리셋을 반환하며 get은 filter().first() 의 의미를 가지고 있습니다. (주의) 만약 여러개의 데이터가 조회되는 경우 MultipleObjectsReturned 에러가 발생하기 때문에 주의가 필요합니다.
> ### board = Board.objects.get(title='제목')

- ## objects.filter()
  - ### 파라미터와 일치하는 여러 객체를 포함하는 QuerySet을 반환합니다.
  - ### filter의 경우 특정 키워드에 매핑되는 객체들을 검색하고 싶은 경우 유용합니다.
> ### board = Board.objects.filter(id = board_id)

## 4) 데이터 수정
- ## objects.update()
  - ### 객체 파라미터로 변경할 데이터를 전달해 DB 데이터를 수정합니다.

## 5) 데이터 삭제
- ## objects.delete()
  - ### 원하는 객체 데이터를 delete() 메서드를 통해 삭제합니다.
  - ### get/filter/all 메서드를 통해 삭제할 데이터를 찾아 해당 데이터를 삭제합니다.
> ### board = Board.objects.get(title="제목") board.delete()

# 3. OR/AND/GROUP BY/ORDER BY
## 1) OR 연산
- ### 두 개 이상의 조건으로 OR 연산하여 검색하고 싶은 경우 아래와 같이 사용합니다.
> ### boards = Board.objects.filter(title="제목") | Board.objects.filter(title="제목2")

## 2) AND 연산
- ### 두 개 이상의 조건으로 결합하여 AND 연산하여 검색하고 싶은 경우 아래와 같이 사용합니다.
> ### boards = Board.objects.filter(title="제목", description="내용")

## 3) GROUP BY
- ### 특정 필드 기준으로 그룹핑한 데이터를 가져오고 싶은 경우 아래와 같이 사용합니다.
> ### Board.objects.filter(title = "제목").group_by('count')

## 4) ORDER BY
- ### 원하는 필드 데이터로 정렬한 데이터를 가져오고 싶은 경우 order_by 메서드를 사용합니다.
- ### 기본 오름차순으로 정렬되며, 내림차순으로 데이터를 꺼내올경우 -(마이너스)를 붙여 가져옵니다.
> ### Board.objects.filter(title = "제목").order_by('-count')

# 4. distinct()
## 1) distinct()를 단독으로 사용
- ### 그럼 distinct()사용해봅시다.
- ### distinct()는 아래와 같이 단체로 사용할 수 있습니다.
> ### Person.objects.distinct()
- ### 모든 객체가 검색되었습니다.
- ###  모델의 모든 필드를 DISTINCT의 조건으로 했을 경우, 중복되는 레코드는 없다는 것입니다.