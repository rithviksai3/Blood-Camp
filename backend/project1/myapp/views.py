from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Detail

# Create your views here.
def index(request):
      if request.method=='POST':
            name=request.POST['name']
            blood_group=request.POST['blood_group']
            mobile_no=request.POST['mobile_no']
            address=request.POST['address']
            print(name,blood_group,mobile_no,address)
            obj=Detail()
            obj.name=name
            obj.blood_group=blood_group
            obj.mobile_no=mobile_no
            obj.address=address
            obj.save()
            messages.error(request,'THANK YOU')
      from django.core import serializers
      data=serializers.serialize("python",Detail.objects.all())
      context={
            'data':data,
      }
      return render(request,'index.html',context)

def delete(request,id):
      event=Detail.objects.get(id=id);
      event.delete()
      return redirect('/index')

def signup(request):
      if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
            if password == password2:
                  if User.objects.filter(email=email).exists():
                       messages.error(request,'Email Already used')
                       return redirect('/')
                  elif User.objects.filter(username=username).exists():
                       messages.error(request,'Username Already exists')
                       return redirect('/')
                  else:
                       user=User.objects.create_user(username=username, email=email,password=password)
                       user.save()
                       return redirect('login')
            else:
                  messages.error(request, 'Password not same')
                  return redirect('/')
      else:
            return render(request,'signup.html') 
      
def login(request):
      if request.method == 'POST':
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            user=auth.authenticate(username=username,email=email,password=password)
            if user is not None:
                  auth.login(request, user)
                  return redirect('index')
            else:
                  messages.error(request, 'username/password is incorrect')
                  return redirect('login')
                  
      else:      
            return render(request,'login.html')

def logout(request):
      auth.logout(request)
      return redirect('/')