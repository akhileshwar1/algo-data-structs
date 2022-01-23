from django.shortcuts import render
from users.forms import RegisterForm
from django.http import HttpResponse
import json
from users.models import User
# Create your views here.


def register(request):
    print("in here")
    print(json.loads(request.body))
    r_form = RegisterForm(json.loads(request.body))
    print(r_form)
    if r_form.is_valid():
        print("in heree")
        r_form.save()
    return HttpResponse("registered")


def login(request):
    print('in login')
    if request.method == 'POST':
        data = json.loads(request.body)
        users = User.objects.get(username=data['username'])
        print(users)
        if users.password == data['password']:
            return HttpResponse('Logged in')
        else:
            return HttpResponse('not valid')
