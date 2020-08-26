#form & import 잘 확인하기***
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('create10/', views.create10, name="create10"), # 자동으로 10개 게시글 만들기
    path('<int:post_id>/', views.detail, name="detail"), #자세히보기
    path('new/', views.new, name="new"), #작성
    path('<int:post_id>/edit/', views.edit, name="edit"), # edit
    path('<int:post_id>/delete/', views.delete, name="delete"), #delete
    path('<int:post_id>/comments/create/', views.comments_create, name="comments_create"), #댓글생성w
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name="comments_delete"), #댓글삭제
    path('<int:post_id>/comments/<int:comment_id>/update/', views.comments_update, name="comments_update"), #댓글수정
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)