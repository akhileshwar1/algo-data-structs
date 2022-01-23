from users import models
from django.forms import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'email', 'password', 'username', 'gender']
