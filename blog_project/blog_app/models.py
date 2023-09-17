from django.db import models
from django.utils import timezone
from uuid import uuid4
import os

def rename_imagefile_to_uuid(instance, filename):

    upload_to = f'uploads'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex
    filename = '{}.{}'.format(uuid, ext)

    return os.path.join(upload_to, filename)




class AttachFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to=rename_imagefile_to_uuid, default='')
    use_yn = models.BooleanField(default=True)
    del_yn = models.BooleanField(default=False)
    write_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    board = models.ForeignKey('Board', models.DO_NOTHING,null=True)

    class Meta:
        db_table = 'attachFile'



class Topic(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    use_yn = models.BooleanField(blank=True, default=True)

    class Meta:
        db_table = 'topic'
class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    use_yn = models.IntegerField(blank=True, default=1)
    del_yn = models.IntegerField(blank=True, default=0)
    write_date = models.DateTimeField(default=timezone.now)
    modif_date = models.DateTimeField(default=timezone.now)
    viewcount = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING, null=True)


    # def save(self, *args, **kwargs):
    #     current_datetime = timezone.now()
    #     self.write_date = current_datetime
    #     super(Board, self).save(*args, **kwargs)



    class Meta:
        db_table = 'board'
