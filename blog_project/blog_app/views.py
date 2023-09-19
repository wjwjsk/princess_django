from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomAuthenticationForm, FileUploadForm, PostWriteForm
from django.urls import reverse_lazy
from .serializers import BoardSerializer
from .models import Topic, Board, AttachFile
from rest_framework import viewsets
from django.http import JsonResponse
import datetime
import json
import openai


# Create your views here.
def index(request):
    topics = Topic.objects.all()
    mvp_topic = request.GET.get("topic")
    if mvp_topic:
        topic = Topic.objects.get(name=mvp_topic)
        most_view_post = Board.objects.filter(topic=topic).order_by("-viewcount").values().first()
        if most_view_post is not None:
            topic_id = most_view_post["topic_id"]
            mtopic = Topic.objects.get(topic_id=topic_id)
        else:
            messages.error(request, "해당 토픽에는 게시글이 없습니다. 게시글 작성 후 확인 가능합니다.")
            return redirect("post_write")

    else:
        most_view_post = Board.objects.order_by("-viewcount").values().first()
        topic_id = most_view_post["topic_id"]
        mtopic = Topic.objects.get(topic_id=topic_id)

    posts = Board.objects.all().order_by("board_id")
    topic = request.GET.get("topic")
    file = AttachFile.objects.all()
    return render(
        request,
        "index.html",
        {
            "topics": topics,
            "most_view_post": most_view_post,
            "mtopic": mtopic,
            "posts": posts,
            "topic": topic,
            "file": file,
        },
    )


def imageUpload(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            attachFileInstance = form.save()

            fileId = attachFileInstance.pk
            fileName = attachFileInstance.file

            data = {"file_id": fileId, "file_path": str(fileName)}

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


def postDtl(request, topic, board_id):
    topics = Topic.objects.all()
    post = Board.objects.get(pk=board_id)
    topic_link = Topic.objects.get(name=topic)
    previous_post = Board.objects.filter(board_id__lt=board_id).order_by("-board_id").first()
    next_post = Board.objects.filter(board_id__gt=board_id).order_by("board_id").first()
    recent_posts = Board.objects.filter(topic=post.topic).order_by("board_id")

    last_view_time_str = request.session.get(f"last_view_time_{board_id}")
    current_time = datetime.datetime.now()

    if not last_view_time_str or (
        current_time - datetime.datetime.strptime(last_view_time_str, "%Y-%m-%d %H:%M:%S.%f")
    ) >= datetime.timedelta(minutes=1):
        post.viewcount += 1
        post.save()
        request.session[f"last_view_time_{board_id}"] = current_time.strftime(
            "%Y-%m-%d %H:%M:%S.%f"
        )

    if request.method == "POST":
        post.delete()
        return redirect("index")

    return render(
        request,
        "post.html",
        {
            "previous_post": previous_post,
            "next_post": next_post,
            "topics": topics,
            "topic_link": topic_link,
            "post": post,
            "recent_posts": recent_posts,
        },
    )


def post_write(request):
    if request.method == "POST":
        form = PostWriteForm(request.POST)
        if form.is_valid():
            board = form.save()
            return redirect("/")
            # return redirect('/post/'+str(board.pk))
        print(form.errors)
        return render(request, "post_write.html")
    elif request.method == "PUT":
        form = PostWriteForm(json.loads(request.body))
        print(request.body)
        body = json.loads(request.body)

        if form.is_valid() == False:
            return JsonResponse({"message": "유효한 겂을 입력해주세요"}, status=400)

        board_id = body["board_id"]
        updated_board = form.update_board(board_id)

        if updated_board == False:
            return JsonResponse({"message": "유효한 겂을 입력해주세요"}, status=400)

        return JsonResponse({"message": "게시글 업데이트 성공", "board_id": str(board_id)}, status=200)
    elif request.method == "DELETE":
        return redirect("/")

    else:
        parameter = {}
        topics = Topic.objects.all()
        parameter["topics"] = topics
        board_id = request.GET.get("board_id")
        if board_id != None:
            board = Board.objects.get(pk=board_id)
            print(board)
            parameter["board"] = board
        return render(request, "post_write.html", parameter)


def chatAi(request):
    if request.method == "POST":
        openai.api_key = ""
        prompt = "질문을 해보자"
        try:
            openai.organization = "org-N6PEQBZRURMASfipxTIHBYw7"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
            # 반환된 응답에서 텍스트 추출해 변수에 저장
            message = response["choices"][0]["message"]["content"]
        except Exception as e:
            message = str(e)
        return JsonResponse({"message": message})
    return JsonResponse({"message": "11"})


def post_list(request, topic=None):
    if topic:
        posts = Board.objects.filter(topic=topic, publish="Y").order_by("-views")

    else:
        posts = Board.objects.filter(publish="Y").order_by("-views")
    return render(request, "blog_app/post_list.html", {"posts": posts})


# def create_or_update_post(request, post_id=None):
#     # 글수정 페이지의 경우
#     if post_id:
#         post = get_object_or_404(Board, id=post_id)

#     # 글쓰기 페이지의 경우, 임시저장한 글이 있는지 검색
#     else:
#         post = Board.objects.filter(author_id=request.user.username, publish='N').order_by('-created_at').first()

#     # 업로드/수정 버튼 눌렀을 떄
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST, instance=post) # 폼 초기화
#         if form.is_valid():
#             post = form.save(commit=False)

#             # 게시물 삭제
#             if 'delete-button' in request.POST:
#                 post.delete()
#                 return redirect('blog_app:post_list')

#             if not form.cleaned_data.get('topic'):
#                 post.topic = '전체'

# post_list에 대한 작업 해야함.
# else:
#     return render(request, "post_write.html")
