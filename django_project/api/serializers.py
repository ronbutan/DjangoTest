from rest_framework import serializers
from blog.models import TbDjangoUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDjangoUser
        fields = ["username","first_name","last_name","password","dob","email"]

