# Branch basic commands

1. 브랜치 생성

   (master) $ git branch {branch name}

2. 브랜치 이동

   (master) $ git checkout {branch name}

3. 브랜치 생성 및 이동

   (master) $ git checkout -b {branch name}

4. 브랜치 목록

   (master) $ git branch

5. 브랜치 삭제

   (master) $ git branch -d {branch name}



# Branch merge

- #### 각 branch에서 작업을 한 이후 커밋과 버전 업을 하기 위해서는 일반적으로 merge 명령어를 사용한다.

- #### 병합을 진행할때, 만약 서로 다른 커밋에서 동일한 파일을 수정한 경우 충돌이 발생할 수 있다. 이 경우에는 반드시 직접 수정을 진행 해야한다.

- #### 충돌이 발생한 것은 오류가 발생한 것이 아니라 커밋이 변경되는 과정에서 반드시 발생할 수 있는것이다.



# Branch merge - fast-forward

- #### 기존 master 브랜치에 변경사항이 없어 단순히 앞으로 이동

  1. feature-a branch로 이동 후 commit
  2. master 별도 변경 없음
  3. master branch로 병합



# Branch merge - merge commit

- #### 기존 master 브랜치에 변경사항이 있어 병합 커밋 발생

  - 같은 파일을 수정 하고 충돌해결하고 같은 파일 수정 못한다.
    1. feature-a branch로 이동 후 commit
    2. master branch commit
    3. master branch로 병합



# Github Flow 기본원칙

- ## Github Flow는 Github에서 제안하는 브랜치 전략으로 다음과 같은 기본 원칙을 가지고 있다. 

  1. master branch는 반드시 배포 가능한 상태여야 한다.
  2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다.
  3. Commit message는 매우 중요하며, 명확하게 작성한다. 
  4. Pull Request를 통해 협업을 진행한다. 
  5. 변경사항을 반영하고 싶다면, master branch에 병합한다.



# Feature Branch Workflow

- ## Shared repository model (저장소의 소유권이 있는 경우)

  1. 다른 사람의 원격저장소에서 folk 한다.
  2. 나의 로컬저장소에 저장한다.
  3. 내가 원하는 내용을 add하고 commit한다.
  4. 그리고 다시 그 다른 사람 원격 저장소에 push 한다.
  5. 그럼 버전 업이 된다.

- ## Forking Workflow (저장소의 소유권이 없는 경우)

  1. 다른 사람의 원격저장소에서 folk 한다.
  2. 나의 로컬저장소에 저장한다.
  3. 내가 원하는 내용을 add하고 commit한다.
  4. 그리고 다시 그 다른 사람 원격 저장소에 push 한다.
  5. 이건 나에게 소유권이 없기 때문에 상대방 한테 제안을 한다.
  6. 상대방이 동의 하면 버전 업되고 동의 안하면 버전 업이 안된다.

