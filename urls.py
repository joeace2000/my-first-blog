from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('comment/<int:pk>/', views.comment_detail, name='comment_detail'),
    path('post/<int:pk>/comment/new/', views.comment_new, name='comment_new'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit')

]