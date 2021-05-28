from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello new"}
    return render(request, 'AppTwo/index.html', context=my_dict)


def help(request):
    help_dict = {'help_insert': "Hello, I'm here to help"}
    return render(request,'AppTwo/help.html', context = help_dict)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'AppTwo/users.html', context = user_dict)