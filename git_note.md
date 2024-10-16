# Git, Github
## 마크다운 (Markdown)
텍스트 기반의 마크업(Markup) 문법
* 마크업 : 태그를 이용하여 문서의 구조를 나타내는 것
* 확장자 : ```.md```
* 사용법
  * 헤딩 : ```#``` 이 많을수록 소제목 (대부분 6개 까지 가능)
  * 리스트
    * Ordered : ```1. 2. 3.```
    * Unordered : ```*```또는 ```-```
  * 코드 블럭
    * 한 줄 코드블럭 : 백틱 ``( ` )`` 을 내용 양 끝에 하나씩 입력
    * 여러 줄 코드블럭 : 백틱 ``( ` )`` 을 내용 양 끝에 세 개 씩 입력
  * 링크 : `[표시되는 문자](url 또는 path)`
    * 예시 : [001.py](git_class/001.py)
  * 이미지 : `![표시되는 문자](url 또는 path)`
    * 예시 : ![snoopy](~/Desktop/hand_snoopy.jpeg)
    * 이미지의 너비와 높이를 직접 조절하는 것은 불가
  * 텍스트 강조 : 텍스트 양 끝에 붙이기
    * **볼드체** : `**` 
    * *이탈릭체* : `*`
    * ~~취소선~~ : `~~`
  * 인용 : `>` 사용
    * 예시
        >인용
        >>인용안에 인용
        >>>인용안에 인용안에 인용
  ___
  * 수평선
    * `---` 또는 `***` 또는 `___` 를 **세 개 이상** 사용
    * 예시
  -------

## Git
: 분산 버전 관리 시스템
* 버전 관리 : 코드의 히스토리 (버전)을 관리하는 도구 
  * 개발되어온 과정을 파악함으로서 이전 버전과의 변경 사항 비교 분석 가능
* 분산 : 중앙 집중형의 반댓말로, 데이터를 보관할 때 데이터에 이상이 생기는 것을 방지하기 위해 여러 곳에 저장하는방법.
  * 하나의 파일을 여러 개 복사해서 저장하는 것이 아님
  * 파일을 하나 그대로 두고 
  * '변경사항' 만을 각 버전으로 가지고 있음
    * Github는 Git 기반의 저장소 서비스

### Linux 명령어 
MacOS의 터미널,
Windows의 Git bash
에서 쓰임

---
* 위치 `~`  : (home directory)내 컴의 홈 위치를 나타냄
  * 예 : `/Users/t2023-m0072`

---
- `ls` 현재 위치의 폴더, 파일 목록 보기
  - `ls -al` : 현재 위치의 숨겨진 폴더, 파일 목록까지
* `pwd` : 현재 위치 보기
- `cd {path}` : 현재 위치 이동하기
    - `cd ~` : 홈 디렉토리로 이동
    - `cd..` : 상위 폴더로 이동
* `mkdir {name}` : (make directory)폴더 생성하기
- `touch {name}` : 파일 생성하기
* `rm {name}` : 삭제하기
    - `rm -r {name}` : 폴더 삭제하기
- `clear`  : 터미널 클리어
* `open .`  : 해당위치의 파일 열기
### Git 기본기
#### Repository

* 특정 디렉토리를 버전 관리하는 저장소
* `git init` 명령어로 로컬 저장소를 생성
  * `.git` 디렉토리가 생기고 이 디렉토리 안에는 버전 관리에 필요한 모든것이 들어있음
  *  !! 바탕화면이나 홈 디렉토리에서 진행하면 해당 디렉토리 안의 많은 파일들을 모두 버전관리하므로 되도록 **특정 디렉토리 안에서 진행**
  
**여기까진 터미널에서 실행**

#### Commit
* 현재 변경 사항을 특정 버전으로 남긴다 == Commit 한다
* 세 가지 영역을 바꿔가며 버전 관리를 함
  * `Working Directory ` 
    * 내가 실제로 작업하고 있는 디렉토리
  - `Staging Area`
    - Commit 으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
  * `Repository`
    * Commit 들이 저장되는 곳

* `git add 파일명` : Commit 만들기 위해 Staging Area 에 추가
* `git commit -m "msg"` : Commit 저장 (msg 부분에 이 커밋을 설명하기)- Repository 에 추가됨
* `git log` : 이 파일의 히스토리를 볼 수 있음
* `git status` : git 상태 보기
  * untracked : 인식 전 - `git add 파일명` 으로 tracked 상태 만들어주기
  * tracked : 인식됨
  * modified : 수정됨
---

* 사용법
  1. 터미널에서 `git init`명령어로 버전 관리 폴더 만들기
  2. 폴더 안에 `test.py` 파일이 있다고 가정하자.
  3. 1번에서 버전관리 폴더를 만들었지만,
  아직 git이 인식하지 않는 상태(Untracked)
  ---
   (여기부턴 VSCode 내의 터미널 사용)

  ---
  1. git 이 버전관리를 시작하게 하기 위해 `git add test.py` 명령어를 입력하여 `Staging Area`에 추가(Tracked)
  2. `git commit -m "msg"`명령어로 버전(Commit)을 `Repository`에 저장 (Committed)
      * 
        ```
        Author identity unknown
        ***
        Please tell me who you are.
        
        Run

        git config --giobal user.email "you@example.com"
        git config --global user.name "Your Name"

        to set your account's default identity.
        ```
        이런 에러가 뜬다면 
        `git config --giobal user.email "you@example.com"` 와
        `git config --global user.name "Your Name"` 로 해당 커밋을 작성한 유저의 정보를 입력해주자

   * 한 번 Tracked 된 파일을 수정하면 수정된 상태 (modified)임
   * 수정 완료시 다시 Commit 하기 ->`git commit -m "msg"`