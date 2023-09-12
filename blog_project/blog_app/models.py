from django.db import models

# Create your models here.


# TOPIC 모델
class Topic(models.Model):
    TOPIC_ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=30)
    USE_YN = models.BooleanField(default=True)

    class Meta:
        db_table = "TOPIC"
        verbose_name = "토픽 정보"
        verbose_name_plural = "토픽 정보"


# BOARD 모델
class Board(models.Model):
    BOARD_ID = models.AutoField(primary_key=True)
    TOPIC_ID = models.ForeignKey(Topic, on_delete=models.CASCADE)
    TITLE = models.TextField()
    CONTENT = models.TextField()
    USE_YN = models.BooleanField(default=True)
    DEL_YN = models.BooleanField(default=False)
    WRITE_DATE = models.DateField()
    MODIF_DATE = models.DateField()
    viewcount = models.IntegerField(default=0)

    class Meta:
        db_table = "BOARD"
        verbose_name = "게시판"
        verbose_name_plural = "게시판"
