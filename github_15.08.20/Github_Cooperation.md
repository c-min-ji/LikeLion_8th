## 자주 쓰는 Git 명령어
| 명령어 | 의미 |
|  :---: | :-----:|
| `git init` | git 저장소를 초기화 |
| `git add . `| 폴더에 변경된 모든 파일 staging area에 올리기|
| `git commit -m "..." `| 유사시 돌아갈 수 있는 저장소의 체크 포인트 생성|
| `git remote add origin 주소`| 원격 저장소 연결| 
| `git branch 브랜치 명`| 새로운 브랜치 생성|
| `git checkout 브랜치 명`| 해당 브랜치로 이동|
| `git push origin 브랜치 명`| 원격 저장소의 특정 브랜치에 프로젝트 저장|
| `git pull origin 브랜치 명`| 원격 저장소의 특정 브랜치에서 변경사항 pull 해오기|
| `git clone 주소` | 원격 저장소에 있는 파일 전체 복사|
| `git status` | git 저장소의 상태 확인|
<br><br><br>
# Github을 통한 협업
1. repo 생성
2. 콜라보레이터 추가하기
    * `setting` -> `manage acess` -> `invite a collaborator` -> invite -> 팀원이 수락하면 끝
3. 초기 프로젝트 push
    * `git init` -> `git remote add origin https://` -> `git add . `-> `git commit -m "first commit"` ->` git push origin master`
4. 팀원들의 로컬에 프로젝트 pull
    * `git clone https:// `
5. 팀원 각자의 브랜치를 생성하여 작업
    * `git branch 이름` -> `git brnach` (생성 확인) -> `git checkout 이름` (이름 브랜치로 체크아웃)
6. 브랜치에 작업한 내용을 push
    * git add . -> git commit -m "메세지" -> git push origin 이름
7. master와 merge 하기 전 pull request
    * `master` 브랜치는 실제 배포 프로그램이 들어있음(고친 거 확인 받기)
    * `pull request` -> `new pull request` -> `base: mater <- compare: 브랜치 이름` -> `create pull request` -> ~~ 바꿨어요! -> `create pull request`
8. pull request 확인 후 master 와 merge
    * master 는 풀리퀘 확인 후 머지 (`merge pull request`) 해줌.
<br><br><br><br>
# 포크(Fork)를 이용한 협업
1. 작업하고 싶은 레포 포크 해오기
    * 레포 들어가서 오른쪽 위 `fork` 버튼 클릭
2. 자신의 로컬에서 작업
    * git clone https:// 
3. 변경사항을 자신의 브랜치에 push
    * git add . -> git commit -m "id change" -> git checkout -b minji(브랜치 생성과 동시에 체크아웃 가능) -> git push origin minji
4. 원본 레포 소유자에게 Pull request 요청
    * pull request -> new pull request -> `base repository: 포크해온레포주소` `base:master` `<-` `head repository: 내 레포주소` `base: minji` -> create pull request
5. 소유자가 pull request를 승인하여 merge  하면 자동으로 collaborator 추가

<br>
<br>

## Github basic & cooperation
[01. github_basic](./github_basic.md)<br>
[02. Netlify](./Netlify.md)<br>
