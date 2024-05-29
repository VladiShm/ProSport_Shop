from django.urls import path

from users.views import login, register,logout

app_name = 'users'

urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]