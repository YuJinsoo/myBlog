from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # 전체 게시물 확인
    path("", views.PostList.as_view(), name="list"),
    # 상세 페이지 조회
    path("<int:post_id>/", views.PostDetail.as_view(), name="detail"),
    # 게시글 작성
    path("create/", views.PostWrite.as_view(), name="write"),
    # 게시글 수정
    path("edit/<int:post_id>/", views.PostEdit.as_view(), name="edit"),
    # 게시글 삭제
    path("delete/<int:post_id>/", views.PostDelete.as_view(), name="delete"),
    # 카테고리 게시글 검색요청
    path("search/", views.PostSearchQuery.as_view(), name="search-query"),
    # 게시글 검색결과
    path("search/<str:cat>", views.PostSearch.as_view(), name="search")
    
    
]
