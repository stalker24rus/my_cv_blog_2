from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .feed import LatestPostsFeed


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<str:author>/<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
    path('<int:post_id>/change/',
         views.post_change, name='post_change'),
    path('<int:post_id>/delete>',
         views.post_delete, name='post_delete'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
    
    path('upload/image', views.upload_image ,name='upload_image'),

    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
    path('post/add', views.post_add, name='post_add'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
