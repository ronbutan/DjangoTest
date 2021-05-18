from django.db import models
from PIL import Image

DEFAULT_IMAGE_FILENAME = "default.jpg"
# Create your models here.
class TbDjangoUser(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    image_file = models.ImageField(upload_to='images/')
    password = models.CharField(max_length=60)
    dob = models.DateField()
    email = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.username} - {self.first_name} - {self.last_name}"

    class Meta:
        managed = False
        db_table = 'tb_django_user'
        ordering = ["first_name","last_name"]



class TbDjangoPost(models.Model):
    post_id = models.CharField(primary_key=True, max_length=35)
    username = models.ForeignKey(TbDjangoUser, on_delete=models.DO_NOTHING, related_name="songs", db_column='username')
    title = models.CharField(max_length=60)
    date_posted = models.DateTimeField()
    content = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.post_id} - {self.username} - {self.title}"

    class Meta:
        managed = False
        ordering = ["-date_posted"]
        db_table = 'tb_django_post'