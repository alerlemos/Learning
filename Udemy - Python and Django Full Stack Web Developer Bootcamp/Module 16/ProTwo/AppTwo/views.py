from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello new"}
    return HttpResponse("<em>My Second App</em>")


def help(request):
    help_dict = {'help_insert': "Hello, I'm here to help"}
    return render(request,'AppTwo/help.html', context = help_dict)
