from django.db import models
from django.utils import timezone


class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True, db_column="topic_id", default="")
    name = models.CharField(max_length=30, db_column="name", unique=True)  # NOT NULL 추가
    use_yn = models.BooleanField(default=True, db_column="use_yn")


class Meta:
    db_table = "TOPIC"
    verbose_name = "토픽 정보"


def str(self):
    return self.name


class Board(models.Model):
    board_id = models.AutoField(primary_key=True, db_column="board_id", default=0)
    topic_id = models.ForeignKey(
        Topic, on_delete=models.CASCADE, db_column="topic_id", to_field="name", default=""
    )
    title = models.TextField(db_column="title", null=False, default="")  # NOT NULL 추가
    content = models.TextField(null=True, blank=True, db_column="content")
    use_yn = models.BooleanField(default=True, db_column="use_yn")
    del_yn = models.BooleanField(default=False, db_column="del_yn")
    write_date = models.DateField(db_column="write_date", null=False, default=timezone.now)
    modif_date = models.DateField(db_column="modif_date", default=timezone.now)
    viewcount = models.IntegerField(default=0)


class Meta:
    db_table = "BOARD"
    verbose_name = "게시판"


def str(self):
    return self.title
