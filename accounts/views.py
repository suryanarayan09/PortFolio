from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['USERNAME']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm_password']
        if User.objects.filter(username=username):
            messages.info(request, 'Username taken')
            return redirect('register')
        elif password!=password2:
            messages.info(request, 'password not matching')
            return redirect('register')

        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                            last_name=last_name)
            user.save()
            return redirect('/')
    else:
        return render(request,'Register.html')


def login(request):
    if request.method=='POST':
        username = request.POST('username')
        password = request.POST('password')
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentiall')
            return redirect('login')

    else:
        return render(request,'login.html')