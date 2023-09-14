from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView



urlpatterns = [
    path(r"", views.index, name="index"),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(r"post", views.post, name="post"),
    path(r"post/<int:board_id>", views.postDtl, name="postDtl"),
    path(r"post/write", views.post_write, name="post_write"),
    path('post/write/upload', views.imageUpload, name='imageUpload'),



]
