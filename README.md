# JS의 Blog

- Django Framework를 사용해 블로그를 개발했습니다.


## 개발 목적

- 게시물과 댓글 등을 작성할 수 잇는 블로그 개발
- Django와 친해지기(**1**/10) 


## 목표와 기능

- 일반적인 블로그가 지원하는 기능을 직접 구현해보았습니다.
- 게시글 CRUD, 댓글 CRD, 로그인 회원가입 로그아웃

1. 메인 페이지 구현
    - 페이지 제목과 블로그 입장 버튼이 있습니다.
    - 회원가입, 로그인 버튼을 통해 회원가입, 로그인 페이지로 이동할 수 있습니다.

2. 회원가입 기능 구현
    - id, password, email을 입력받아 계정을 생성합니다.

3. 로그인 기능 구현
    - 회원가입한 계정으로 로그인 할 수 있습니다.

4. 게시글 작성 기능 구현
    - 로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.
    - 사진 업로드가 가능 합니다.
    - 게시글 조회수가 올라갈 수 있도록 합니다. (쿠키 이용)

5. 게시글 목록 기능 구현
    - 모든 사용자들이 게시한 블로그 게시글들의 제목을 확인 할 수 있습니다.

6. 게시글 상세보기 기능 구현
    - 게시글의 제목/내용을 보는 기능입니다.

7. 게시글 검색 기능 구현
    - 주제와 태그에 따라 검색이 가능하게 합니다.
    - 검색한 게시물은 시간순에 따라 정렬이 가능해야 합니다.

8. 게시글 수정 기능 구현
    - 로그인을 한 유저만 해당 기능을 사용 할 수 있습니다.
    - 글 작성자 혹은 관리자가 아니라면 수정이 불가능합니다.
    - 업로드한 이미지를 게시물에서 제외할 수(삭제할 수) 있습니다.

9. 게시글 삭제 기능 구현
    - 게시글 작성자 혹은 관리계정만 수정 및 삭제가 가능합니다.
    - 삭제를 완료한 이후에 게시글 목록 화면으로 돌아갑니다.
    - 삭제된 게시글은 게시글 목록보기/상세보기에서 접근이 불가능하고 url로 접근 시 `존재하지 않는 게시글입니다` 라는 페이지를 보여줍니다.

10. 댓글 기능
    - 댓글 작성 및 삭제 기능을 구현했습니다.
    - 대댓글 작성 및 삭제 기능을 구현했습니다. (depth는 1 단계만)

11. 마이페이지 기능
    - 회원만의 Profile 생성 및 수정 기능을 구현했습니다.
    - 계정의 비밀번호를 변경하는 기능을 구현하였습니다. (PasswordChangeForm)
    - 비밀번호 변경 후 로그인 유지 기능 구현하였습니다.(update_session_auth_hash)


## 개발 일정

- 개발 기간 : 2023년 7월 17일 ~ 7월 20일 + a

## 개발 환경

- Language : Python, JavaScript
- Framework : Django
- IDE : VScode
- ETC : HTML, CSS, Bootstrap5

## 프로젝트 구성

- 메인 앱
  - myapp
  - 프로젝트

- blog 앱
  - blog
  - 블로그 관련 기능, 블로그 페이지

- user 앱
  - user
  - 유저 관련 페이지, 기능

- my_setting.py : django key 숨김
- requirement.txt : 설치 모듈

- 폴더트리 (vscode extension : file-tree-generator 사용)
```
📦myBlog
 ┣ 📂blog
 ┃ ┣ 📂migrations
 ┃ ┣ 📂static
 ┃ ┃ ┗ 📂blog
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📂blog
 ┃ ┃ ┃ ┣ 📜404.html
 ┃ ┃ ┃ ┣ 📜post_detail.html
 ┃ ┃ ┃ ┣ 📜post_edit.html
 ┃ ┃ ┃ ┣ 📜post_list.html
 ┃ ┃ ┃ ┣ 📜post_search.html
 ┃ ┃ ┃ ┗ 📜post_write.html
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂media
 ┃ ┗ 📂images
 ┣ 📂myapp
 ┃ ┣ 📂static
 ┃ ┃ ┗ 📂myapp
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜my_setting.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┃ ┗ 📂css
 ┣ 📂templates
 ┃ ┣ 📜base.html
 ┃ ┣ 📜footer.html
 ┃ ┣ 📜index.html
 ┃ ┗ 📜navbar.html
 ┣ 📂user
 ┃ ┣ 📂static
 ┃ ┃ ┗ 📂user
 ┃ ┣ 📂templates
 ┃ ┃ ┗ 📂user
 ┃ ┃ ┃ ┣ 📜user_login.html
 ┃ ┃ ┃ ┣ 📜user_mypage.html
 ┃ ┃ ┃ ┗ 📜user_register.html
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂venv
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜README.md
 ┗ 📜requirement.txt

```

### 사이트맵 - 마인드맵

![마인드맵](/readme/mindmap.jpg)

- 프로젝트를 시작할 때 어떤 기능을 구현할 지 구조적으로 확인하는 차원에서 마인드 맵으로 표현한 다음 프로젝트 구현을 시작했습니다.
- 마인드맵으로 표현해보니 어떤 페이지로 이동되고, 어떤 기능이 그 페이지에 들어있어야 하는지 정리되었습니다.
- 페이지 수가 많아지고 복잡해지면 그리기 어려울 것 같다는 생각을 했습니다.

### ERD - DB 구조

![ERD](/readme/erd_db.png)


- DB 설계입니다.
- 총 6개의 테이블로 작성했습니다.
- 게시글(Post), 유저(User), 댓글(Comment), 대댓글(Recomment), 프로필(Profile), 카테고리(Category)로 구성되어 있습니다.
- 카테고리를 게시글에서 분리한 이유는 새로운 카테고리 삭제하거나 추가하는 기능을 추가할 때 확장성을 위해 정규화 하였습니다.
- 댓글과 대댓글 테이블을 분리했습니다. 댓글 자체에 부모 댓글을 주어 구현하는 방법과 고민했는데, 댓글 대댓글의 종속 관계를 확실히 하고 페이지 렌더링에서 편의를 보기 위해 선택했습니다. 또한 추후 대댓글을 숨김처리해서 원할때 불러오도록 해서 쿼리 효율성을 높일 수 있을 것이라고 기대했습니다.


## 동작 화면

- 메인화면, 회원가입, 로그인, 블로그창

![캡쳐1](/readme/1.gif)

- 메인에서 블로그창, 글작성
    - 줄바꿈 무시 현상이 있어서 `pre`태그 사용
![캡쳐1](/readme/2.gif)

- 댓글 작성/삭제, 대댓글 작성/삭제

![캡쳐1](/readme/3.gif)

- 글 수정, 삭제

![캡쳐1](/readme/4.gif)

- 삭제된 글 조회시.. 

![캡쳐1](/readme/5.gif)

- 조회수. 중복안되는것까지

![캡쳐1](/readme/6.gif)

- 게시글 카테고리 조회

![캡쳐1](/readme/7.gif)



## 개발 이슈

- 이번 프로젝트에서 인상깊게 느꼈던 부분은 **조회수** 기능과 **이미지 업로드** 기능이었습니다.

- 대댓글
    - 대댓글은 댓글에 답변을 달린다는 개념으로 생각했고, 그래서 대댓글 모델(ReCommnet)을 새로 만들었습니다.
    - 대댓글은 어떤 댓글에 달린 것인지 알아야 하기 때문에 댓글과 내용, 시간을 필드로 가지게 했습니다.
    - 시간이 많이 걸렸던 부분은 댓글에 대댓글을 달 수 있는 폼을 생성하는 부분이었습니다.
    - JavaScript를 이용해서 노드를 찾고 원하는 위치에 폼을 추가하는 방식으로 진행했습니다.

- 게시물 검색
    - 기존에는 검색어를 전달하기 위해 다른 뷰를 거쳐치는 방식으로 개발했었습니다. 하지만 이 방식은 뷰가 2번 호출되므로 비효율적인 방식이라고 생각했습니다. (검색 한 번에 view를 하나 더 타고 가는것은 일반적이지 않은 방법이라고 판단했습니다.)
    - 그래서 `PostSearch` 를 개발하였습니다. 
    - 쿼리 파라메터로 검색 내용을 보내 해당 내용을 포함하는 제목을 가진 Post들을 검색하는 기능으로 구현했습니다.
    - 템플릿은 post_list.html를 공통으로 사용했습니다.
    - 페이지네이션 기능이 구현되도록 적용했습니다.

- 조회수 
    - 조회수 기능은 단순히 게시물 조회 할 때 `hits`를 +1 해 주는 방식으로는 가짜 조회수가 무수히 늘어나게 됩니다.
    - 이런 현상을 방지하는 방법에 대해 찾아보다가 쿠키/ 로컬스토리지 / ip저장 이렇게 세 가지 방법 알게 되었습니다.
    - ip저장은 db 테이블을 새로 만들어야 했고, 로컬스토리지는 js에 많이 의존하게 되었습니다. 그래서 간편하면서 속도가 빠른 `쿠키` 방법이 가장 적합하다고 생각했습니다.
    - 이 과정에서 django의 `view`에 들어오는 `request`에는 **쿠키**와 **세션** 과 같은 다양한 정보들이 함께 전달되는 것을 알게되었고, 쿠키와 세션을 잘 이해해야 유연한 웹 비스를 만들 수 있을 것 같다고 느꼈습니다. (쿠키와 세션을 이용한...)

- 이미지업로드
    - 게시글 이미지 업로드 기능을 개발하면서 html 의 `form` 태그에 `enctype` 어트리뷰트가 설정이 필요하다는 것을 알게 되었습니다.
    - request에 이미지 파일 정보가 들어가려면 `enctype` 어트리뷰트를 `multipart/form-data` 로 설정해 주어야 했습니다.
    - 또한 글 수정시 이미지를 넣어주지 않으면 기존에 들어갔던 이미지가 사라지는 현상이 발생했습니다.
    - 그래서 form에 hidden input을 주어서 기존 이미지 url을 보내는 방법으로 해당 이슈를 해결했습니다.
    - 서버 개발은 유저의 요청을 잘 처리하는 프로그램을 만드는 것이므로, 유저의 요청을 주는 `폼 태그`와 `request`에 대해 잘 이해하고 있어야겠다고 느꼈습니다.

- 두 포인트 모두 view단에서 처리하는 `request`에 관련된 내용이었네요.

- 페이지네이션
    - 게시판을 효과적으로 정리해서 볼 수 있는 pagination 기능을 개발한 것이 기억에 남습니다.
    - 첫 입장, 카테고리별 검색, 글 검색 등 환경에서 모두 동일한 페이지에 표시해야 했습니다.
    - 그래서 여러 함수에 pagination이 중복적으로 개발되어있는데, 중복을 최소화 할 수 있는 방법이 있는지 공부가 필요하다고 느껴졌습니다.

- Django의 Form 활용하는 방법
  - 결국 서버의 동작의 요점은 유저의 input을 포함한 요청을 처리하고 응답해주는 것이라는 것을 다시 한번 깨닫게 되었습니다.
  - 유저의 Input을 `form` 태그를 이용해 받게 되므로, Django에서 지원해주는 form 기능을 유연하게 활용하는 것이 중요하다고 느꼈습니다.
  - 프론트 부분에 `Bootstrap5`를 적용했는데 이 부분을 form에 적용하기 위해해 widget 속성에 css 클래스를 부여하는 방식으로 적용했습니다.



## 추가 개발할 내용

1. LightSail 배포해보기 (진행 중)
2. profile 및 회원정보 수정 (완료) >> 이미지 제거 기능 추가 필요
3. 내가작성한 게시물 리스트 보기 기능 (완료) >mypage에 modal로 추가
4. 글작성시 toast ui 넣어보기
5. 이미지 여러개 업로드
6. 글 수정시 현재 올라간 이미지 이름 표시해주기(완료) >> 이미지 제거 기능 추가 필요(완료)
7. 글 제목/내용/작성자 내용으로 검색기능 - (글내용 검색 추가)
8. 게시판 pagenation (완료)
9. 카테고리 검색에서 카테고리 버튼을 클릭해서 찾는 기능으로 변경(완료)


# 느낀점

- 장고를 사용해서 혼자 개발해보는 프로젝트가 처음이라서 재미있었습니다. 
- 어떤 기능을 구현할 때 방법이 생각나지 않거나 방법을 구현하는 방법을 찾지 못할 때에는 다소 답답함을 느꼈습니다. 
- 하지만 기능 개발에 초점을 맞추고 하나씩 해결하는 과정에서 뿌듯함을 느꼈습니다.
- 모르는 기능을 개발 할 때에는 다른 사람 코드를 많이 참고하게 되었는데 어서 익숙해져서 내 코드로 만들고 싶어졌습니다.
- 제공된 UI 템플릿을 사용했으면 훨씬 예쁘게 되지 않았을까 하는 아쉬움이 남았습니다.
- 배포쪽에는 손을 대지 못해서 아쉬웠습니다.
- Django ORM이 중요하다는 것을 알게되었다. ORM을 잘 다루는 방법과 쿼리가 어떻게 생성되는지 궁금해졌습니다.
- Form의 에러 표현 방법 밋 Form 다루는 법. 결국 서버로 데이터를 주고받는 창은 Form 이므로 Form을 잘 활용하는 것이 중요하다고 느껴졌습니다.

## 힘들었던 점

1. 블로그를 개발하면서 **개발 일정과 순서를 정하는 것이 어려웠습니다.** 프로젝트가 어느정도 볼륨인지 감이 오지 않아서 일정 설정에 어려움이 있었습니다. 블로그를 개발 할 때 필요한 기능은 다양하고, 그 기능들은 방향으로 연결되어 있습니다. 그러다 보니 하나의 기능을 개발하는 도중 다른 기능이 눈에 들어와서 다른 기능을 개발하다가 다시 원래 개발하려는 기능으로 돌아왔을 때, 어떻게 개발했었는지 로딩시간이 필요했습니다. 이런 일이 빈번하게 발생하다보니 개발 속도도 더디고 머리속이 혼란스러워졌습니다. 이런 문제가 발생하는 원인은 개발 숙련도와 집중력이 문제라고 생각했습니다. 

  > 하나의 기능만 포커스하여 골격을 잡는다는 생각으로 집중하는 방식으로 개선했습니다. 중요한 줄기가 연결될때 까지는 다른 기능에 대한 방법이 보이더라도 현재 개발하는 코드에 집중하려고 노력했습니다.

  > 어서 장고에 익숙해져서 능숙하게 개발 순서를 정하고 차근차근 개발할 수 있는 개발자가 되고 싶습니다.

2. UI를 생성하거나 꾸미는부분이 조금 어려웠던것 같습니다. 템플릿으로 전달받은 파일들이 있지만, 어떻게 적용시켜야 할 지 이리저리 헤메다가 시간을 많이 소비했습니다. 전달받은 css파일들을 스태틱 파일에 어떻게 배치해야 하는지 등에 대한 고민이었습니다. 

  > 스태틱 파일들에 대한 관리도 중요하다고 생각했지만, 일단은 지금 이 프로젝트에서 ui가 가장 중요한 것은 아니라고 판단했습니다.

  > UI 템플릿을 사용하면 더 이쁘게 개발했겠지만, 어떻게 손을 대야할 지 감이 오지 않았고, tailwind는 간단하게 했었지만, bootstraop으로 ui를 만들어 본 적은 없었습니다. 때문에 이참에 bootstrap을 사용해보자고 생각해서 bootstrap을 사용했습니다. 지금 할 수 없는 것에 포커스를 맞춰서 스트레스 받기보다 다른 방법을 빠르게 생각해내서 적용하는 것이 중요하다고 느꼈습니다.

3. AWS의 LightSail에서 서버 인스턴스를 생성하고 해당 컴퓨팅 리소스를 서버로 세팅하는데 생각보다 많은 어려움이 있었습니다. Linux에 대해 아직 익숙하지 않은 상황이라 어디서부터 시작해야 하는지 감이 오지 않았습니다.
  > 구글링을 통해 하나씩 해보았습니다.