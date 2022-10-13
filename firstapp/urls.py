from django.contrib import admin
from django.urls import include, path
from firstapp import views

urlpatterns = [
    path('',views.first,name='first'),
    path('login_fun',views.login_fun,name='login_fun'),
    path('signup_fun',views.signup_fun,name='signup_fun'),
    path('user_create',views.user_create,name='user_create'),
    path('user_login',views.user_login,name='user_login'),
    path('adminpage_fun',views.adminpage_fun,name='adminpage_fun'),
    path('teacher_fun',views.teacher_fun,name='teacher_fun'),
    path('addcourse_fun',views.addcourse_fun,name='addcourse_fun'),
    path('add_course',views.add_course,name='add_course'),
    path('showstudent_fun',views.showstudent_fun,name='showstudent_fun'),
    path('addstudent_fun',views.addstudent_fun,name='addstudent_fun')
]