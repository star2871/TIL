# Git 의 개요

- Git은 분산버전관리시스템으로 코드의 버전을 관리하는 도구이다.
- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율한다.



# 분산버전관리시스템(DVCS)

- 분산버전관리시스템은 원격 저장소를 통합 협업하고, 모든 히스토리를 클라이언트들이 공유한다.

  | 원격 저장소 |
  | :---------: |
  |  version 1  |
  |  version 2  |
  |  version 3  |

  ![화면 캡처 2022-07-06 170713](Git 의 특징.assets/화면 캡처 2022-07-06 170713.png)

| computer A | computer B |
| :--------: | :--------: |
| version 1  | version 1  |
| version 2  | version 2  |
| version 3  | version 3  |

서로 서로 버전을 풀 푸쉬 할 수 있다.

# Git 의 기본 명령어

## $ git init

특정 폴더를 git 저장소(repository)를 만들어 git으로 관리

- git 폴더가 생성된다.
- git bash에서는 (master)라는 표기를 확인 할 수 있다.

Working directory에서 add를하면 staging area에 임시 저장되고 commit 하면 버전이 기록된다.



## $ git add <file>

- working directoy상의 변경 내용을 staging area에 추가하기 위해 사용된다.



## $ git commit -m '<커밋메시지>'

- staged 상태의 파일들을 커밋을 통해 버전으로 기록한다.

- commit 이해하기
  - Git은 데이터를 파일 시스템의 스냅샷으로 관리하고 매우 크기가 작다.
  - 파일이 달라지지 않으면 성능을 위해 파일을 새로 저하지 않는다.



## $ git log

- 현재 저장소에 기록된 커밋을 조회한다.
- 다양한 옵션을 통해 로그를 조회할 수 있다.
  - $ git log -1
  - $ git log --oneline
  - $ git log -2 --oneline



## $ git status

- staging area에 있는 파일을 확인 할 수 있다.



# git 사용시

## 저장소 만들고 첫번째 버전 기록하기

1. 바탕화면에 test 폴더를 만들고 git 저장소를 만들기 
2. a.txt 파일 넣고 커밋하기 
3. 임의의 파일을 만들고 커밋하기
4.  a.txt 파일 수정하고 커밋하기



## TIL 프로젝트 관리

1. TIL 폴더를 만들고 git 저장소를 만들기 

2. README.md 파일을 만들고 커밋하기 

3. 오늘 작성한 마크다운 파일을 옮기고 커밋하기 
   1. 마크다운 파일별로 각각 커밋을 진행해보세요!
4.  이제까지 배운 내용들을 정리하고 커밋하기