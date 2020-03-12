
from django.urls import path
from .import views


urlpatterns = [
    path('', views.default_page, name='default-page'),
    path('posts/', views.main_page, name="main-page"),
    path('posts/<int:pk>/', views.post_detail, name="post-detail"),
    path('posts/create/', views.post_create, name="post-create"),
    path('posts/<int:pk>/delete/', views.post_delete, name="post-delete"),
    path('posts/<int:pk>/update/', views.post_update, name="post-update"),
    path('posts/<int:pk>/likes/', views.liked_users, name='liked-users'),
    path('posts/post/delete-comment/<int:pk>/', views.delete_comment, name='delete-comment'),
    path('posts/post/update-comment/<int:pk>/', views.update_comment, name='update-comment'),
    
]
