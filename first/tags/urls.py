
from django.urls import path
from .import views


urlpatterns = [
    path('', views.tags_list, name="tags-list"),
    path('<int:pk>/', views.tag_detail, name="tag-detail"),
    path('create/', views.tag_create, name="tag-create"),
    # path('<int:pk>/delete/', views.tag_delete, name="tag-delete"),
    # path('<int:pk>/update/', views.tag_update, name="tag-update"),
]
