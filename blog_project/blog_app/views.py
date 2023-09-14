from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_view
from django.http import JsonResponse
from .models import Topic, Board, AttachFile
from .forms import CustomAuthenticationForm, FileUploadForm




# Create your views here.
def index(request):
    topics = Topic.objects.all()
    most_view_post = Board.objects.order_by("-viewcount").values().first()
    posts = Board.objects.all()
    return render(
        request, "index.html", {"topics": topics, "most_view_post": most_view_post, "posts": posts}
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


class CustomLoginView(auth_view.LoginView):
    form_class = CustomAuthenticationForm


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
    print(1)


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
        return render(request, 'post_write.html')

