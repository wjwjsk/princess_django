from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "GET":
        # TODO 로그인 페이지 로 이동
        # return render(request, '로')
        print(1)
    elif request.method == "POST":
        # TODO 로그인시 메인페이로 이동
        return redirect('/')



    # 목록
def post(request):
    topic = request.GET['topic']

    if(topic is None):
        return render(request, 'postWrite.html')
        print(1)
    else:
        print(1)
    

    # 상세
def postDtl(request,board_id):
    print(1)



def postWrite(request):
    if request.method == "POST":
        # 글쓰기
        # code...
        return render(request, 'postWrite.html')
    elif request.method == "PUT":
        # 글 수정
        # code...
        return render(request, 'postWrite.html')
    elif request.method == "DELETE":
        # 글 삭제
        # code...
        return redirect('/')
    else: 
        return render(request, 'post_write.html')

    
