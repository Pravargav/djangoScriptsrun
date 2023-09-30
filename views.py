
from django.shortcuts import render

def index(request):
    context={}
    return render(request, 'takeTest/index.html', context)




