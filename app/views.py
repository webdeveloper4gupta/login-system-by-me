from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import booking
from .forms import bookingform
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='home')
def bookings(request):
    form=bookingform()

    if request.method=="POST":
        n1=request.POST.get('name')
        id=request.user.id
        n2=request.POST.get('fromto')
        n3=request.POST.get('destination')
        n4=request.POST.get('phno')
        n5=request.POST.get('email')
        book=booking(name=n1,fromto=n2,destination=n3,phno=n4,email=n5,userid=id)
        book.save()
        n=booking.objects.filter(userid=id)
    
    
        
        return render(request,"check.html",{'book':n})


    return render(request,"booking.html",{'forms':form,})



def home(request):
    if request.method=='POST':
        n1=request.POST.get('name')
        n2=request.POST.get('password')
        
        user=authenticate(username=n1,password=n2)

        if user is not None:
            login(request,user)
            return redirect('bookings')
        else:
            messages.error(request,"invalid credentials")
    return render(request,"home.html")
def signout(request):
    logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect('home')


def signup(request):
    if request.method=="POST":
        n1=request.POST.get('n1')
        n2=request.POST.get('n2')
        n3=request.POST.get('n3')
        n4=request.POST.get('n4')

        # here do some custom validation
        if User.objects.filter(username=n1):
            messages.error(request,"username already eexist")
            return redirect('signup')
        
        if User.objects.filter(email=n2):
            messages.error(request,"already exist ")
            return redirect('signup')
        
        if len(n1)<2:
            messages.error(request,"name must more then 2 character")
            return redirect('signup')
        myuser=User.objects.create_user(n1,n2,n4)
        myuser.save()

        messages.success(request,"hurray your  account has been succesfully created.")

        return redirect("home")


    return render(request,"signup.html")
