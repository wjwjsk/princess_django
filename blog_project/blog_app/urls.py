from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path(r'', views.index, name='index'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(r'post', views.post, name='post'),
    path(r'post/<int:board_id>', views.postDtl, name='postDtl'),
    path(r'post/write', views.post_write, name='post_write'),
]