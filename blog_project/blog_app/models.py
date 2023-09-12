from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True, db_column="topic_id")
    name = models.CharField(max_length=30, db_column="name", null=False)  # NOT NULL 추가
    use_yn = models.BooleanField(default=True, db_column="use_yn")
    
    class Meta:
        db_table = "topic"
        verbose_name = "토픽 정보"


class Board(models.Model):
    board_id = models.AutoField(primary_key=True, db_column="board_id")
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE, db_column="topic_id")
    title = models.TextField(db_column="title", null=False)  # NOT NULL 추가
    content = models.TextField(null=True, blank=True, db_column="content")
    use_yn = models.BooleanField(default=True, db_column="use_yn")
    del_yn = models.BooleanField(default=False, db_column="del_yn")
    write_date = models.DateField(db_column="write_date", null=False)  # NOT NULL 추가
    modif_date = models.DateField(db_column="modif_date", null=False)  # NOT NULL 추가
    viewcount = models.IntegerField(default=0)
    
    class Meta:
        db_table = "board"
        verbose_name = "게시판"
