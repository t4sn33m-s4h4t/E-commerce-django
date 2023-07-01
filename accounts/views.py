from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
def not_logged_in(user):
  return not user.is_authenticated

# Create your views here.
@user_passes_test(not_logged_in, '/')
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        if not user_obj.exists():
            messages.warning(request, "Account not found.")
            return HttpResponseRedirect(request.path_info)
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "Your account is not verified.")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = email, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')
        messages.warning(request, "Invalid credentials.")

    return render(request, 'accounts/login.html')

@user_passes_test(not_logged_in, '/')
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        if user_obj.exists():
            messages.warning(request, "This email is already taken.")
            return HttpResponseRedirect(request.path_info)
        user_obj = User.objects.create(first_name = first_name, last_name=last_name, email=email, username = email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, "Check you email to verify.")

    return render(request, 'accounts/register.html')

@login_required(login_url='accounts/login/')
def logout_page(request):
    logout(request)

    return redirect('/')


@login_required(login_url='accounts/login/')
def profile_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        messages.success(request, "Your profile has been updated.")



    return render(request, 'accounts/profile.html')
def activate_email(request, email_token):
    try: 
        user = Profile.objects.get(email_token = email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Envalid Email Token')