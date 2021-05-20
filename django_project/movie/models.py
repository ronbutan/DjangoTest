from datetime import datetime
from django.db import models

# Create your models here.
class TbCs605Rating(models.Model):
    rating_cd = models.CharField(primary_key=True, max_length=30)
    rating_desc = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tb_cs605_rating'

class TbCs605Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    classification = models.CharField(max_length=60)
    running_time = models.IntegerField()
    box_office_uom = models.CharField(max_length=1, default="m")
    box_office = models.FloatField()
    release_date = models.DateField()
    date_last_upd = models.DateTimeField(editable=False,default=datetime.now())
    image_file = models.ImageField(null=True,upload_to='images/')
    synopsis = models.CharField(max_length=4096)

    class Meta:
        managed = False
        db_table = 'tb_cs605_movie'
        ordering = ["-release_date"]

class TbCs605Genre(models.Model):
    movie = models.ForeignKey(TbCs605Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tb_cs605_genre'
        unique_together = (('movie', 'genre'),)

class TbCs605Subtitle(models.Model):
    movie = models.ForeignKey(TbCs605Movie, on_delete=models.CASCADE)
    seq_no = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    subtitle = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'tb_cs605_subtitle'
        unique_together = (('movie', 'seq_no'),)

TbCs605Rating.objects = TbCs605Rating.objects.using("cs605")
TbCs605Movie.objects = TbCs605Movie.objects.using("cs605")
TbCs605Genre.objects = TbCs605Genre.objects.using("cs605")
TbCs605Subtitle.objects = TbCs605Subtitle.objects.using("cs605")