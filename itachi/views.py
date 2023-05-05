from django.shortcuts import render,HttpResponse,redirect
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

def home(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')

def logins(request):
    return render(request,'login.html')

def doLogin(request):
    if request.method == "POST":
        user=EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            user_type=user.user_type
            if user_type =='1':
                return redirect('adminhome')
            elif user_type =='2':
                return redirect('facultyhome')
            elif user_type =='3':
                return redirect('studenthome')
            else:
                messages.error(request,'Invalid Credentials !')
                return render('login')
        else:
            messages.error(request,'Invalid Credentials !')
            return redirect('login')
        
def doLogout(request):
    logout(request) 
    return redirect('login')

@login_required(login_url='/')
def profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    context={
        "user":user,
    }
    return render(request,'profile.html',context)

@login_required(login_url='/')
def profileupdate(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        # email=request.POST.get('email')
        # username=request.POST.get('username')
        password=request.POST.get('password')
        
        try: 
            customuser=CustomUser.objects.get(id = request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            
            if password != None and password != "":
                customuser.set_password(password)
            if profile_pic != None and profile_pic != "":
                 customuser.profile_pic=profile_pic
            customuser.save()
            messages.success(request,'Your Profile Updated Successfully !')
            return redirect('profile')
            
        except:
            messages.error(request,'Failed to update your profile!')
        
    return render(request,'profile.html')