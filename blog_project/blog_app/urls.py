from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'login', views.login, name='login'),
    path(r'post', views.post, name='post'),
    path(r'post/<int:board_id>', views.postDtl, name='postDtl'),
    path(r'post/write', views.postWrite, name='postWrite'),
]