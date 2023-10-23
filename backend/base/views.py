from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import json
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


# Create your views here.
def home(request):

    return render(request, "authentication/index.html")



def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')

        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()

        refresh = RefreshToken.for_user(myuser)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.data.get('username')
        pass1 = request.data.get('pass1')
        address = request.data.get('address')  # Get the address from the request data

        user = authenticate(username=username, password=pass1)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'address': address
            })

        return Response({'error': 'Bad Credentials'}, status=400)

    return render(request, "authentication/signin.html")


def sign(request):

    data1 = request.session.get('user')
    data3 = request.session.get('address')
    data = {'dict2': json.dumps({'user_name': data1,'address': data3})}
    print(data)
    return render(request, "authentication/sign.html", data)


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')