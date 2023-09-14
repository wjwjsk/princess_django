from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    use_yn = models.BooleanField(blank=True, default=True)

    class Meta:
        db_table = 'topic'


class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    use_yn = models.BooleanField(blank=True, null=True)
    del_yn = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(auto_now_add=True)
    modif_date = models.DateTimeField(blank=True, null=True)
    viewcount = models.IntegerField()
    topic = models.ForeignKey('Topic', models.DO_NOTHING)

    class Meta:
        db_table = 'board'
