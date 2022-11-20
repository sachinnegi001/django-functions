from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages                         #to import the messages functionality
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, logout,login, update_session_auth_hash #to update for every logout  
from django.contrib.auth.decorators import login_required

from datetime import datetime
from app.models import Profile


def home(request):
    return render(request, "home.html")


def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user:
            login(request, user)  
            return HttpResponseRedirect("/profile")
        else:
            return render(request, 'signin.html',{"status":"invalid credentials"})
    else: 
     return render(request, "signin.html")


def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phonenumber = request.POST['phonenumber']
        dateofbirth = request.POST['dateofbirth']
       

        if User.objects.filter(username=username).exists():
            messages.info(request, "this username is already taken.....")
            return redirect('signup')

        elif User.objects.filter(email=email).exists():
            messages.info(request, "this email-id is already registered.....")
            return redirect('signup')
        else:
            usr = User.objects.create_user(username=username, email=email, password=password)
            usr.save()
            
            profile=Profile(user=usr,email=email,dateofbirth=dateofbirth,phonenumber=phonenumber)
            profile.save()
            dates=profile.dateofbirth
            birthdayyear=int(dates[0]+dates[1]+dates[2]+dates[3])
            today = datetime.now()
            todayyear =int( today.strftime("%Y"))
            final_age=todayyear-birthdayyear
           
            
            profile.age=final_age
            profile.save()
        return redirect("signin")
    return render(request, "signup.html")


def profiles(request):
    
    if request.user.is_authenticated:
        pro = Profile.objects.get(user__id=request.user.id)
        
        context = {'proff':pro}
        return render(request, "profile.html",context)
    else:
        messages.info(request, "Login First.....")
        return redirect("signin")
    return render(request, "profile.html")
    
    
def editprofiles(request):
    if request.user.is_authenticated:
        pro = Profile.objects.get(user__id=request.user.id)
        context = {'proff':pro}
        
        if request.method == "POST":
            uname = request.POST["username"]
            email = request.POST["email"]
            phonenumber = request.POST["number"]
            birthday = request.POST["birthday"]
            
            usr = User.objects.get(id=request.user.id)
            
            usr.username=uname
            usr.save()
            

            
            pro.dateofbirth="none"
            pro.dateofbirth=birthday
            pro.email=email
            pro.phonenumber=phonenumber
            pro.save()
            dates=pro.dateofbirth
            birthdayyear=int(dates[0]+dates[1]+dates[2]+dates[3])
            today = datetime.now()
            todayyear =int( today.strftime("%Y"))
            final_age=todayyear-birthdayyear
            pro.age=final_age
            pro.save()
            
            if "image" in request.FILES:
                img = request.FILES["image"]
                pro.file= img
                pro.save()
                
                
            context["status"]="changes saved successful"
            
        
        return render(request, "editprofile.html",context)
    else:
        messages.info(request, "Login First.....")
        return redirect("signin")
    return render(request, "editprofile.html")

@login_required
def logout_user(request):
    logout(request)
   
    return  redirect("home")
