from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('s1/', views.subject1, name='subject1'),
    path('s2/', views.subject2, name='subject2'),
    path('s3/', views.subject3, name='subject3'),
    path('s4/', views.subject4, name='subject4'),

    path('s1/',include([
        path('theory1/', views.theory1),
        path('radio1/', views.radio1),
        path('checkbox1/', views.checkbox1),
    ])),
    path('s2/',include([
        path('theory2/', views.theory2),
        path('radio2/', views.radio2),
        path('checkbox2/', views.checkbox2),
    ])),
    path('s3/',include([
        path('theory3/', views.theory3),
        path('radio3/', views.radio3),
        path('checkbox3/', views.checkbox3),
    ])),
    path('s4/',include([
        path('theory4/', views.theory4),
        path('radio4/', views.radio4),
        path('checkbox4/', views.checkbox4),
    ])),
      
] 