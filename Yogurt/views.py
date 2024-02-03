from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    menu=Product.objects.all()
    return render(request,'menu.html',{'menu':menu})

def login_user(request):
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request,username=username, password=password)
       if user is not None:
           login(request, user)
           messages.success(request,('You have been logged in'))
           return redirect('home')
       else:
           messages.success(request,('There was an error,please try again...'))
           return redirect('login')
   else:
        return render(request,'login.html',{})
    
def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out'))
    return redirect('home')

def product(request,pk):
    product=Product.objects.get(id=pk)
    print(product)
    return render(request, 'product.html',{'product':product})

def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("You Have Registered Successfully!! Welcome!"))
			return redirect('home')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})
def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form=UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request,('Your profile has been updated'))
            return redirect('home')
        return render(request, 'update_user.html', {'user_form':user_form})
    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('home')

def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method == 'POST':
            form=ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ("Your Password Has Been Changed!!"))
                login(request,current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form=ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})
    else:
        messages.success(request, ("You Must Be Logged In To Access That Page!!"))
        return redirect('home')
