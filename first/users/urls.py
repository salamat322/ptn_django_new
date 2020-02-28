
from django.urls import path
from .import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_user, name='user-login'),
    path('logout/', LogoutView.as_view(next_page="main-page"), name="user-logout"),
    # path('<int:pk>/', views.user_detail, name="user-detail"),
    path('signup/', views.signup, name="user-create"),
    # path('<int:pk>/delete/', views.tag_delete, name="tag-delete"),
    # path('<int:pk>/update/', views.tag_update, name="tag-update"),
]
