from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import CustomLoginView
from rest_framework.routers import DefaultRouter
from .views import BoardViewset

router = DefaultRouter()
router.register(r"Board", BoardViewset)



urlpatterns = [
    path(r"", views.index, name="index"),
    path(r"login/", CustomLoginView.as_view(template_name="registration/login.html"), name="login"),
    path(r"logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(r"post", views.post, name="post"),
    path(r"post/<int:board_id>", views.postDtl, name="postDtl"),
    path(r"post/write", views.post_write, name="post_write"),
    path('post/write/upload', views.imageUpload, name='imageUpload'),
    path(r"api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)