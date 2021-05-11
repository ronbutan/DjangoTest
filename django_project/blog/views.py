from django.shortcuts import render
from blog.models import TbDjangoUser, TbDjangoPost
from django.db import connection

# Create your views here.
def home(request):
    
    sql = "SELECT post_id,username,title,date_posted,content FROM django.tb_django_post"
    cursor = connection.cursor()
    cursor.execute(sql)
    posts = []
    for (post_id,username,title,date_posted,content) in cursor:
        user = TbDjangoUser()
        user.username = username
        post = TbDjangoPost()
        post.post_id = post_id
        post.username = user
        post.title = title
        post.date_posted = date_posted
        post.content = content
        posts.append(post)
    context = {
        "posts": posts
    }
    return render(request, template_name="blog/home.html", context=context)

def about(request):
    return render(request, template_name="blog/about.html",context={"title":"About"})

def adduser(request):
    if request.method == "POST":
        print(f"Data: {request.POST}")
        if request.POST.get("username") and request.POST.get("password") and request.POST.get("email"):
            username = request.POST.get("username").lower()
            firstname = request.POST.get("firstname").upper()
            lastname = request.POST.get("lastname").upper()
            password = request.POST.get("password")
            dob = request.POST.get("dob")
            email = request.POST.get("email")
            print(f"Received {username}, {password}, {email} from adduser.")
            user = TbDjangoUser()
            user.username = username
            user.first_name = firstname
            user.last_name = lastname
            user.password = password
            user.dob = dob
            user.email = email
            insert_stmt = (
                "INSERT INTO django.tb_django_user (username,first_name,last_name,password,dob,email) "
                "VALUES (%s, %s, %s, %s, %s, %s)"
            )
            cursor = connection.cursor()
            cursor.execute(insert_stmt, (username,firstname,lastname,password,dob,email))
            return render(request, template_name="blog/adduser.html",context={"title":"Add User"})
    else:
        return render(request, template_name="blog/adduser.html",context={"title":"Add User"})

