from django import forms
from .models import TbDjangoUser

class TbDjangoUserForm(forms.ModelForm):
    class Meta:
        model = TbDjangoUser
        fields = ["username","first_name","last_name","image_file","password","dob","email"]