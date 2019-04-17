from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Portraits,Cityseapes,Nature
from django.core.paginator import Paginator
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Create your views here.
def home(request):
    portrait=Portraits.objects.all()
    paginator = Paginator(portrait,1)
    page = request.GET.get('page')
    portraits = paginator.get_page(page)

    cityseape=Cityseapes.objects.all()
    paginator = Paginator(cityseape,1)
    page = request.GET.get('page')
    cityseapes = paginator.get_page(page)

    nature=Nature.objects.all()
    paginator = Paginator(nature,1)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    text={
        'portraits':portraits,
        'cityseapes':cityseapes,
        'nature':contacts,
    }
    if request.method == 'POST':
        if request.user.is_authenticated:
            messages.success(request,'Accept your message')
            return redirect('home')
        else:
            messages.error(request, 'Unauthenticated person ,Register First ')
            return redirect('registers')
    else:
        return render(request,'second/home.html',text)

# POst details >>>>>>>>>>>>>>>>>>>>>>>>
def detail(request,slug):
    portraits=Portraits.objects.get(slug=slug)
    texts={
        'portraits': portraits,
    }
    return render(request,'second/details.html',texts)


# Register def >>>>>>>>>>>>>>>>>>>>>>>>................................

def registers(request):
    if request.method == 'POST':
        #Get form value
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check if password mach
        if password == password2:
            #cheack username
            if User.objects.filter(username=username).exists():
                messages.error(request,'This username is being used')
                return redirect('registers')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'this email is being used')
                    return redirect('registers')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    # login after user
                    user.save()
                    messages.success(request,'You are now registerd and you can login . ')
                    return redirect('login')
        else:
            messages.error(request,'Password not match')
            return redirect('registers')
    else:
        return render(request,'second/registers.html')

# LOgin def >>>>>>>>>>>>>>>>>>>>>>>>................................
def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('Your have been logged !'))
            return redirect('home')

        else:
            messages.success(request, ('Error logging in Please Try Again !'))
            return redirect('login')

    else:
        return render(request,'second/login.html')

#LogOut >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out ! '))
    return redirect('home')