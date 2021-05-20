#from django_project import movie
import re
from django.shortcuts import render
from .models import *
from django.db import connection
import srt
import datetime

# Create your views here.
def index(request):
    movies = TbCs605Movie.objects.all()
    ratings = TbCs605Rating.objects.all()
    # sql = "SELECT post_id,username,title,date_posted,content FROM django.tb_django_post"
    # cursor = connection.cursor()
    # cursor.execute(sql)
    # posts = []
    # for (post_id,username,title,date_posted,content) in cursor:
    #     user = TbDjangoUser()
    #     user.username = username
    #     post = TbDjangoPost()
    #     post.post_id = post_id
    #     post.username = user
    #     post.title = title
    #     post.date_posted = date_posted
    #     post.content = content
    #     posts.append(post)
    context = {
        "movies": movies,
        "ratings": ratings
    }
    return render(request, template_name="movie/index.html", context=context)

def create(request):
    movies = None
    ratings = None
    if request.method == "GET":
        ratings = TbCs605Rating.objects.all()
    elif request.method == "POST":
        movie_id = request.POST.get("movie_id")
        title = request.POST.get("title")
        classification = request.POST.get("classification")
        box_office = request.POST.get("box_office")
        running_time = request.POST.get("running_time")
        release_date = request.POST.get("release_date")
        synopsis = request.POST.get("release_date")
        image_file = request.FILES.get("image_file")
        movie = TbCs605Movie(movie_id=movie_id,title=title,classification=classification,box_office=box_office,
                            running_time=running_time,release_date=release_date,synopsis=synopsis,image_file=image_file)
        movie.save(using="cs605")

        srt_file = request.FILES.get("srt_file")
        content = srt_file.read()
        content = str(content, "utf-8")
        subtitle_generator = srt.parse(content)
        subtitles = list(subtitle_generator)

        insert_stmt = (
            "INSERT INTO cs605.tb_cs605_subtitle (movie_id,seq_no,start_time,end_time,subtitle) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        cursor = connection.cursor()
        

        for subtitle in subtitles[:10]:
            # hour,minute,second_micro = subtitle.start.split(":")
            # second, microsecond = second_micro.split(".")
            
            start = subtitle.start.total_seconds()
            end = subtitle.end.total_seconds()
            cursor.execute(insert_stmt, (movie_id,subtitle.index,start,end,subtitle.content))

    context = {
        "movies": movies,
        "ratings": ratings
    }
    return render(request, template_name="movie/addmovie.html", context=context)

def update(request,pk):
    movie = None
    ratings = []
    if request.method == "GET":
        movie = TbCs605Movie.objects.get(movie_id=pk)
        ratings = TbCs605Rating.objects.all()

    context = {
        "movie": movie,
        "ratings": ratings
    }
    return render(request, template_name="movie/updmovie.html", context=context)