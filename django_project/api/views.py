from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import UserSerializer
from django.db import connection, DatabaseError
from blog.models import TbDjangoUser


# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/user-list/",
        "Detail View": "/user-detail/<str:pk>/",
        "Create": "/user-create/",
        "Update": "/user-update/<str:pk>/",
        "Delete": "/user-delete/<str:pk>/",
    }

    return Response(api_urls)

@api_view(["GET"])
def userlist(request):
    sql = "SELECT username,first_name,last_name,password,dob,email FROM django.tb_django_user"
    cursor = connection.cursor()
    cursor.execute(sql)
    users = []
    for (username,first_name,last_name,password,dob,email) in cursor:
        user = TbDjangoUser()
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.password = password
        user.dob = dob
        user.email = email
        users.append(user)
    cursor.close()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def userDetail(request, pk):
    user = TbDjangoUser.objects.get(username=pk)
    # sql = "SELECT username,first_name,last_name,password,dob,email FROM django.tb_django_user WHERE username = %s"
    # cursor = connection.cursor()
    # try:
    #     cursor.execute(sql, (pk,))
    # except DatabaseError as dbe:
    #     print(type(dbe.args))
    #     msg = f"DB error [{dbe.args[0]}]"
    #     return JsonResponse({"message":msg})
    # except TypeError as te:
    #     print(f"Message: {te.args}")
    #     return JsonResponse({"message":"db error"})
    # except:
    #     print("Something wrong!!")
    #     JsonResponse({"message":"something wrong"})
    # (username,first_name,last_name,password,dob,email) = cursor.fetchone()
    # user = TbDjangoUser()
    # user.username = username
    # user.first_name = first_name
    # user.last_name = last_name
    # user.password = password
    # user.dob = dob
    # user.email = email
    # cursor.close()
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    print(f"SERIALIZER: {serializer}")
    if serializer.is_valid():
        username = request.data.get("username").lower()
        firstname = request.data.get("first_name").upper()
        lastname = request.data.get("last_name").upper()
        password = request.data.get("password")
        dob = request.data.get("dob")
        email = request.data.get("email")
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
    return Response(serializer.data)

@api_view(["POST"])
def userUpdate(request, pk):
    u = TbDjangoUser.objects.get(username=pk)
    serializer = UserSerializer(instance=u, data=request.data)
    print(f"SERIALIZER: {serializer}")
    print(f"Valid: {serializer.is_valid()}")
    #if serializer.is_valid():
    username = request.data.get("username").lower()
    firstname = request.data.get("first_name").upper()
    lastname = request.data.get("last_name").upper()
    password = request.data.get("password")
    dob = request.data.get("dob")
    email = request.data.get("email")
    print(f"Received {username}, {password}, {email} from adduser.")
    user = TbDjangoUser()
    user.username = username
    user.first_name = firstname
    user.last_name = lastname
    user.password = password
    user.dob = dob
    user.email = email
    update_stmt = (
        "UPDATE django.tb_django_user SET first_name = %s, last_name = %s, dob = %s, email = %s "
        "WHERE username = %s"
    )
    cursor = connection.cursor()
    cursor.execute(update_stmt, (firstname,lastname,dob,email,username))
    return Response(serializer.data)

@api_view(["DELETE"])
def userDelete(request, pk):
    u = TbDjangoUser.objects.get(username=pk)
    m = str(u)
    u.delete()
    return Response(m)
