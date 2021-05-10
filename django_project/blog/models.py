from django.db import models

# Create your models here.
class TbDjangoPost(models.Model):
    post_id = models.CharField(primary_key=True, max_length=35)
    username = models.ForeignKey('TbDjangoUser', models.DO_NOTHING, db_column='username')
    title = models.CharField(max_length=60)
    date_posted = models.DateTimeField()
    content = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'tb_django_post'


class TbDjangoUser(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    image_file = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    dob = models.DateField()
    email = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.username} - {self.first_name} - {self.last_name}"

    class Meta:
        managed = False
        db_table = 'tb_django_user'
