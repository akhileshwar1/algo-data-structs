from django.urls import path
from users.views import register, login


app_name = 'users'
urlpatterns = [
    path('register', register),
    path('login', login)
]
