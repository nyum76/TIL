# Git 특강  2

* Q. Staging Area 가 왜 있을까?( 바로 Commit 하면 편할텐데 )
* A. 변경 사항이 있을 때, 전체를 커밋하지 않고 원하는 변경사항들만 커밋 할 수 있도록

## Remote Repository
* Remote Repo 와 Local Repo 를 연결하는 법
  * 첫번째 방법 : 로컬 레포지토리에게 리모트 레포지토리 위치를 알려주기
    * `git remote add origin {remote_repo}`
    * 내가 갖고있는 커밋 올리기 : `git push origin main`
      * 여기서 처음이면 로그인해야함
      * origin : remote name
    * 두번째 방법 : 깃에서 만들어진 리모트 레포를 로컬 레포로 가져오기
* git은 commit 을 단위로 작동-> commit 을 push

  ---
### TIL 프로젝트
* 내가 매일 배운 내용을 마크다운으로 정리해서 문서화하기
* github 관리 첫 걸음
* 1 일 1 커밋!
* 신입 개발자에게 요구하는 것 중하나! : 꾸준히 성작 (학습)할 수 있는가?