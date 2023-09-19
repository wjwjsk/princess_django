from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import AttachFile, Board, Topic


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = AttachFile
        fields = ["file"]


class PostWriteForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["title", "content", "topic", "use_yn"]

    topic = forms.ModelChoiceField(queryset=Topic.objects.all())

    def update_board(self, board_id):
        # 폼에서 전달된 데이터로 게시글 업데이트
        title = self.cleaned_data["title"]
        content = self.cleaned_data["content"]
        topic = self.cleaned_data["topic"]

        try:
            board = Board.objects.get(board_id=board_id)
            board.title = title
            board.content = content
            board.topic = topic
            board.save()
            return board  # 업데이트된 게시글 객체 반환
        except Board.DoesNotExist:
            return None  # 게시글을 찾을 수 없을 때 None 반환


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {"invalid_login": ("아이디 또는 비밀번호가 올바르지 않습니다. 다시 확인해 주세요.")}

    def __init__(self, request=None, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = ""
        self.fields["username"].widget.attrs["placeholder"] = "아이디"
        self.fields["password"].label = ""
        self.fields["password"].widget.attrs["placeholder"] = "패스워드"


class BlogPostForm(forms.ModelForm):
    class Meta:
        # model = BlogPost
        exclude = ["created_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["topic"].required = False
        self.fields["publish"].required = False
        self.fields["views"].required = False
