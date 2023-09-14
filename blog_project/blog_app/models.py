from django.db import models
import os
from uuid import uuid4

def rename_imagefile_to_uuid(instance, filename):

    upload_to = f'uploads'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex
    filename = '{}.{}'.format(uuid, ext)

    return os.path.join(upload_to, filename)

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    use_yn = models.BooleanField(blank=True, default=True)

    class Meta:
        db_table = 'topic'


class AttachFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=rename_imagefile_to_uuid, default='')
    use_yn = models.BooleanField(default=True)
    del_yn = models.BooleanField(default=False)
    write_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    board = models.ForeignKey('Board', models.DO_NOTHING,null=True)

    class Meta:
        db_table = 'attachFile'




class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    use_yn = models.BooleanField(blank=True, null=True)
    del_yn = models.BooleanField(blank=True, null=True)
    write_date = models.DateField()
    modif_date = models.DateField(blank=True, null=True)
    viewcount = models.IntegerField()
    topic = models.ForeignKey('Topic', models.DO_NOTHING)

    class Meta:
        db_table = 'board'
