from django.urls import re_path
from . import views

urlpatterns = [
    re_path('board/$', views.BoardPostList.as_view()),
    re_path('search/$', views.SearchComment.as_view()),
    re_path('comments/$', views.CommentListCreate.as_view()),
    re_path('posts/$', views.PostListCreate.as_view()),
    re_path('posts/(?P<post_id>[0-9]+)/$', views.PostRetrieveUpdateDestroy.as_view()),
]