from django.shortcuts import render

# Create your views here.
def index(request):
    index_dict = {'insert_content': "First App"}
    return render(request, 'first_app/index.html', context=index_dict)
