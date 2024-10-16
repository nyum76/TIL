# Git.Github

## Git
: 분산 버전 관리 시스템
#### commit 의 세 가지 영역
  * Working Directory : 작업 폴더
    * `git add 파일명` : 해당 파일을 Staging Area 로 옮김
    * `git add .`: 모든 파일을 Staging Area 로 옮김
  * Staging Area : 하나의 버전으로 만들기 위해 머무는 공간
    * `git commit -m "커밋메세지"` : tracked 되어있는 파일(들)을 Commit 으로 남기기
  * Repository : 커밋이 저장되는 공간 (저장소)
    * Local Repository : 내 컴퓨터에서 생성한 레포지토리
      * `git init` 명령어로 로컬 저장소 생성
        * `.git` 디렉토리가 생김
    * Remote Repository : 
  
---

Q. Staging Area 가 왜 있을까?( 바로 Commit 하면 편할텐데 )
A. 변경 사항이 있을 때, 전체를 커밋하지 않고 원하는 변경사항들만 커밋 할 수 있도록. Commit 으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일들을 두는 곳

---

#### terminal 로 git commit 실습
   * 바탕화면에 edu_git_commit 폴더 만들고 git 저장소 생성
   * 해당 폴더 안에 a.txt 라는 텍스트 파일을 만들고, "add a.txt" 라는 커밋메세지로 커밋 생성
   * b.txt 라는 텍스트 파일을 만들고, "add b.txt"라는 커밋메세지로 커밋 생성
   * a.txt 파일 수정 후 "update a.txt" 라는 커밋메세지로 커밋 생성
     * 예시 ![example](<edt_git_commit_example 2.png>)

---

## Github 
: Remote Repository 중 하나
#### Remote Repository
: Local Repository 와 Remote Repository 를 연결해보기
* github 에 로그인 
* 오른쪽 상단의 프로필 클릭 - 'Your Repositories' 클릭 후, 'New' 로 레포지토리 생성
  * 되도록 Public 으로 하고 밑의 README 파일 생성 여부는 해도되고 안 해도 됨. 다른것은 대부분 건드리지 말 것.
* 첫 번째 방법 : 로컬 레포지토리가 이미 있는 상태에서 리모트 레포지토리에게 그 위치를 알려주기
  * terminal 에 `git remote add origin 리모트레포지토리주소` 입력
    * 예시 : `git remote add origin https://github.com/nyum76/TIL`
  * `git push origin main` 입력
  * Username 과 Password 를 입력하는 칸이 나왔다면, 자신의 깃허브 닉네임을 입력.
    * PASSWORD에는 깃허브-우측상단프로필-Settings-Developer Settings-Personal access tokens-Tokens(classic)-Generate new token-new toekn(classic)
    - 해당 토큰 이름 설정 후 밑 선택지에서 repo 체크박스를 전체선택한 후 생성
    - 토큰 복사 
    -  다시 터미널에 들어가서 Password 에 방금 복사한 토큰 붙여넣기
* 두 번째 방법 : 깃허브에서 만든 Remote Repository 를 Local Repository 로 가져오기
  * Github 에서 가져오려는 레포지토리의 주소 복사 후
  * 터미널에 `git clone 복사한레포지토리주소`
    * 예시 : `git clone https://github.com/nyum76/TIL`
    * **주의사항 : master or main, 즉, Git 으로 버전 관리가 되고 있는 폴더 안에 또 다른 저장소를 만드는 것은 안 됨**
    * 따라서 **cd 명령어를 사용해 위치를 desktop으로 옮겨서 진행**
  * 이제 갖고온 리모트레포지토리 폴더가 생성된 것을 볼 수 있음 ( `ls` 명령어 사용 )
  * 이제 이 곳에 파일을 만들고 커밋을 진행.
    * `git add 파일명`
    * `git commit -m "커밋메세지"`
  * 앞의 내용을 진행하여 커밋을 남겼다면
  * push 진행 
    * `git push` or `git push origin main`
  * Github에 가서 페이지를 새로고침하면 Commit 된 내용이 반영된 것을 볼 수 있음
---
##### Github 프로필 꾸미기
* username 과 똑같은 이름의 Repository 생성 (README 파일 생성 여부 선택 해야함)
* VSCode 에서 README.md 파일에 Markdown 형식으로 작성
* 터미널에 add commit push 모두 진행하면
* 내 Github 프로필에 README 파일의 내용이 반영 됨

구글링으로 'Github 프로필 꾸미기' 검색해서 나온 글들 참고해서 맘에 드는 것으로 꾸밀 수도 있음

---

##### Github Pages
: Github 에서 제공하는 무료 웹 호스팅 서비스로, Github Repo 와 연동되어 push 하면 즉각적으로 반영됨

###### 하는 방법!
* `username.github.io`이름의 Repo 만들기
* clone 받아서 index.html 파일 작성
  * index.html 파일을 VSCode 에서 열고 !입력후 `tab` 하면 자동 완성됨
* add commit push 후, https://username.github.io 들어가보기
* index.html 을 수정 후 다시 push
* (선택)https://startbootstrap.com 에서 템플릿 받아서 해보기





---
###### 참고할 만한 링크
* [git push 할 때마다 password](https://velog.io/@kya754/Git-pull-push-%ED%95%A0-%EB%95%8C-password-%EB%A7%A4%EB%B2%88-%EC%9E%85%EB%A0%A5%ED%95%98%EA%B8%B0-%EA%B7%80%EC%B0%AE%EB%8B%A4%EB%A9%B4)

* [Authentication failed 해결과 토큰 발급 방법](https://yian.tistory.com/38)
* [깃, 깃허브 강의 : Github 로 포트폴리오 작성법](https://www.youtube.com/watch?v=lelVripbt2M)
* [Github 로 포트폴리오 작성법](https://www.youtube.com/watch?v=SZcjvjrdomE)