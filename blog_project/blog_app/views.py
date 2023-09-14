from django.shortcuts import render, redirect
from .models import Topic, Board
from django.contrib.auth import views as auth_view
from .forms import CustomAuthenticationForm
from .forms import BlogPostForm
from .models import Board
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def index(request):
    topics = Topic.objects.all()
    most_view_post = Board.objects.order_by("-viewcount").values().first()
    posts = Board.objects.all()
    return render(
        request, "index.html", {"topics": topics, "most_view_post": most_view_post, "posts": posts}
    )


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


def post_list(request, topic=None):
    
    if topic:
        posts = Board.objects.filter(topic=topic, publish='Y').order_by('-views')
    
    else:
        posts = Board.objects.filter(publish='Y').order_by('-views') 
    return render(request, 'blog_app/post_list.html', {'posts': posts})




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