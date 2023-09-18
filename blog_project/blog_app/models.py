from django.db import models
from django.utils import timezone
from uuid import uuid4
import os


def rename_imagefile_to_uuid(instance, filename):
    upload_to = f"uploads"
    ext = filename.split(".")[-1]
    uuid = uuid4().hex
    filename = "{}.{}".format(uuid, ext)

    return os.path.join(upload_to, filename)


class AttachFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=rename_imagefile_to_uuid, default="")
    use_yn = models.BooleanField(default=True)
    del_yn = models.BooleanField(default=False)
    write_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    board = models.ForeignKey('board', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = "attachFile"


class Topic(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    use_yn = models.BooleanField(blank=True, default=True)

    def get_all_topics():
        return Topic.objects.all()

    class Meta:
        db_table = "topic"


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    use_yn = models.BooleanField(blank=True, default=True)
    del_yn = models.BooleanField(blank=True, default=False)
    write_date = models.DateTimeField(default=timezone.now)
    modif_date = models.DateTimeField(default=timezone.now)
    viewcount = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, null=True)


    def update_board(_board):
        board = Board.objects.get(pk=board_id)
        if board:
            board.title = _board.title
            board.content = _board.content
            board.topic_id = _board.topic
            board.use_yn = _board.use_yn
            board.topic = _board.topic
            board.save()
            return True
        return False


    # def save(self, *args, **kwargs):
    #     current_datetime = timezone.now()
    #     self.write_date = current_datetime
    #     super(Board, self).save(*args, **kwargs)

    class Meta:
        db_table = "board"
