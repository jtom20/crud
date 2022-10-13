from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import student_details,course_details

from firstapp.models import usermember

# Create your views here.

def first(request):
    return render(request,'home.html')

def login_fun(request):
    return render(request,'login.html')

def signup_fun(request):
    return render(request,'signup.html')

def adminpage_fun(request):
    return render(request,'profile.html')

def teacher_fun(request):
    return render(request,'teacher.html')

def addcourse_fun(request):
    course=course_details.objects.all()
    return render(request,'addcourse.html',{'course':course})

def showstudent_fun(request):
    stud = student_details.objects.all()
    return render(request,'student.html',{'stud':stud})

def addstudent_fun(request):
    return render(request,'addstudent.html')









def user_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        user_name = request.POST.get('uname')
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        if request.FILES.get('img') is not None:
            image = request.FILES.get('img')
        else:
            image = '/static/image/default.png'
        
        if password==cpassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'This Username already exists')
                return redirect('signup_fun')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=user_name,
                    password=password,
                    email=email,
                )
                user.save()
            userprofile = usermember(user_address=address,user_gender=gender,user_mobile=mobile,user_photo=image)
            userprofile.save()
            subject = 'Hi Welcome aboard'
            body = 'HI this is a automated mail. The University Welcomes you to its new e-Platform for handling details of the students.'    
            send_mail(subject,body, settings.EMAIL_HOST_USER, [email])
        else:
            messages.info(request, 'Passwords is not matching ')
            return redirect('signup_fun')
        return redirect('login_fun')
    return render(request, 'signup.html')


def user_login(request): 
    try:
        if request.method == 'POST':
            try:
                username = request.POST['uname']
                password = request.POST['pass']
                user = auth.authenticate(username=username, password=password)
                #request.session["uid"] = user.id
                if user is not None:
                    if user.is_superuser:
                        auth.login(request, user)
                        return redirect('adminpage_fun')
                    else:
                        auth.login(request, user)
                        messages.info(request, f'Welcome {username}')
                        return redirect('teacher_fun')
                else:
                    messages.info(request, 'Invalid username or password')
                    return redirect('login_fun')
            except:
                messages.info(request, 'Invalid username or password')
                return render(request, 'login.html')
        else:
            # messages.info(request, 'Invalid username or password')
            return render(request, 'login.html')
    except:
        messages.info(request, 'Invalid username or password')
        return render(request, 'login.html')
    
def add_course(request):
    if request.method=='POST':
        cors=request.POST['course']
        cdue=request.POST['cdue']
        cfee=request.POST['cfee']
        crs=course_details()
        crs.course_name=cors
        crs.duration=cdue
        crs.fee=cfee
        crs.save()
        print("hii")
        return redirect('addcourse_fun')
    

        




        