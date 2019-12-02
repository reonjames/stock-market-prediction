from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
	return render(request,'home.html',{})
def signup(request):
	if request.method == 'POST':
		
		
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		question=request.POST.get('question')
		answer=request.POST.get('answer')
		print (name,email,password)
		
		# name1 = UserProfile.objects.filter(name=name).exists()
		email1 = UserProfile.objects.filter(email=email).exists()
		
		if not email1:

			user1 = User.objects.create_user(
				username=email,
				password = password 

				)
			# user1.save()
			user = UserProfile.objects.create(
				user=user1,
				name=name,
				email=email,
				question=question,
				answer=answer,
				password=password,
			)

			return render(request, 'login.html', {})
		else:               
			return render(request, 'signup.html', {})
	else:
		return render(request, 'signup.html',{})
def login(request):
	if request.method=="POST":
		email=request.POST.get('email')
		password=request.POST.get('password')
		# user = authenticate(username=email, password=password)
		# email1=UserProfile.objects.filter(email=email).exists()
		passw1=UserProfile.objects.filter(password=password).exists()
		print("$$$$$$$$$$$$$$$$$$$$$$$$$")
		print(passw1)
		if passw1:
			return render(request,'home.html',{})
		else:
			return render(request,'signup.html',{})
	else:
		return render(request,'login.html',{})	
def forget(request):
	if request.method=="POST":
		name=request.POST.get('name')
		ans=request.POST.get('answer')
		anser=UserProfile.objects.filter(answer=ans).exists()
		if anser:
			post=UserProfile.objects.get(name=name)
			return render(request,'remem.html',{'post':post})			
	else:
		return render(request,'forget.html',{})		