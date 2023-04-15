
from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question1,Question2,Question3,Question4

def index(request):
    context={}
    return render(request, 'takeTest/index.html', context)

def subject1(request):
    context={}
    return render(request, 'takeTest/subject1.html', context)

def subject2(request):
    context={}
    return render(request, 'takeTest/subject2.html', context)

def subject3(request):
    context={}
    return render(request, 'takeTest/subject3.html', context)

def subject4(request):
    context={}
    return render(request, 'takeTest/subject4.html', context)

def theory1(request):
    question_list=Question1.objects.all()
    # io = '\n'.join([q.qn for q in question_list])
    context={'question_list':question_list}
    return render(request,'takeTest/t1.html',context)

def theory2(request):
    question_list=Question2.objects.all()
    # io = '\n'.join([q.qn for q in question_list])
    context={'question_list':question_list}
    return render(request,'takeTest/t2.html',context)

def theory3(request):
    question_list=Question3.objects.all()
    # io = '\n'.join([q.qn for q in question_list])
    context={'question_list':question_list}
    return render(request,'takeTest/t3.html',context)

def theory4(request):
    question_list=Question4.objects.all()
    # io = '\n'.join([q.qn for q in question_list])
    context={'question_list':question_list}
    return render(request,'takeTest/t4.html',context)

def radio1(request):
    context={}
    return render(request, 'takeTest/r1.html', context)

def radio2(request):
    context={}
    return render(request, 'takeTest/r2.html', context)

def radio3(request):
    context={}
    return render(request, 'takeTest/r3.html', context)

def radio4(request):
    context={}
    return render(request, 'takeTest/r4.html', context)

def checkbox1(request):
    context={}
    return render(request, 'takeTest/c1.html', context)

def checkbox2(request):
    context={}
    return render(request, 'takeTest/c2.html', context)

def checkbox3(request):
    context={}
    return render(request, 'takeTest/c3.html', context)

def checkbox4(request):
    context={}
    return render(request, 'takeTest/c4.html', context)







