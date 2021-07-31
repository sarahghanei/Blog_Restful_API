from django.urls import path
from .views import *

urlpatterns = [
    # user patterns
    path('users/', UserList.as_view(), name='User_List'),
    path('users/<int:pk>/', UserDetail.as_view(), name='User_Detail'),
    # post patterns
    path('posts/', PostList.as_view(), name='Post_List'),
    path('posts/<int:pk>', PostDetail.as_view(), name='Post_Detail'),
    # comment patterns
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    # category patterns
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
]
