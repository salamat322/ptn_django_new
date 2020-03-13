from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import Profile


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if pass1 == pass2:
            user = User.objects.create(
                username=username, 
                email=email)
            user.set_password(pass1)
            user.save()
            
            Profile.objects.create(user=user)

            user = authenticate(username=username, password=pass1)
            login(request, user)
            return redirect('main-page')
        else:
            messages.success(request, "Password are not similar")
    return render(request, "signup.html")   


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main-page')
        except:
            print("No such user")

    return render(request, 'login.html')
        



def user_profile(request, pk):
    user_obj = User.objects.get(pk=pk)
    user_profile = Profile.objects.get(user=user_obj)
    if request.method == "POST":
        bio = request.POST.get("bio")

        user_profile.bio = bio
        user_profile.save()
        return redirect(user_profile.get_absolute_url())
    return render(request, 'user_profile.html', locals())


    