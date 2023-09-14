from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, FileUploadForm
from django.urls import reverse_lazy
from .serializers import BoardSerializer
from .models import Topic, Board, AttachFile
from rest_framework import viewsets
from django.http import JsonResponse


# Create your views here.
def index(request):
    topics = Topic.objects.all()
    most_view_post = Board.objects.order_by("-viewcount").values().first()
    posts = Board.objects.all()
    topic = request.GET.get('topic')
    return render(
        request, "index.html", {"topics": topics, "most_view_post": most_view_post, "posts": posts, 'topic': topic}
    )



def imageUpload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():

            attachFileInstance = form.save()

            fileId= attachFileInstance.pk
            fileName = attachFileInstance.file

            data = {'file_id': fileId, 'file_path': str(fileName)}

        return JsonResponse(data)

class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return self.request.GET.get("next", reverse_lazy("/"))



class CustomLoginView(auth_view.LoginView):
    form_class = CustomAuthenticationForm


class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    


# def login(request):
#     if request.method == "GET":
#         # TODO 로그인 페이지 로 이동
#         return render(request, 'login.html')
#         print(1)
#     elif request.method == "POST":
#         # TODO 로그인시 메인페이로 이동
#         return redirect("/")

#     # 목록


def post(request):
    topic = request.GET["topic"]

    if topic is None:
        return render(request, "post_write.html")
        print(1)
    else:
        print(1)

    # 상세


def postDtl(request, board_id):
    post = Board.objects.get(id=board_id)
    pnum = post.id
    return render(request, "postDtl.html", {"pnum": pnum})


def post_write(request):
    if request.method == "POST":
        # 글쓰기
        # code...
        return render(request, "post_write.html")
    elif request.method == "PUT":
        # 글 수정
        # code...
        return render(request, "post_write.html")
    elif request.method == "DELETE":
        # 글 삭제
        # code...

        return redirect("/")
    else:
        return render(request, "post_write.html")
