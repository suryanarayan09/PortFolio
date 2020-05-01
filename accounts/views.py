from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from UserInfo.models import *

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
        elif User.objects.filter(email=email):
            messages.info(request,'email taken')
            return redirect('register')

        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                            last_name=last_name)
            user.save()
            auth.login(request,user)
            Portfolio = PortFolio.objects.filter(user=1)
            for portfolio in Portfolio:
                paragraph_about = portfolio.paragraph_about
                showcase_content = portfolio.showcase_content
                showcase_image = portfolio.showcase_image
                about_image = portfolio.about_image
            users = request.user
            portfolio = PortFolio(user=users, paragraph_about=paragraph_about, showcase_content=showcase_content,
                                  showcase_image=showcase_image, about_image=about_image)
            portfolio.save()
            return redirect('/')
    else:
        return render(request,'Register.html')


def login(request):
    if request.method=='POST':
        username = request.POST['USERNAME']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentiall')
            return redirect('login')

    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    print(request.user.username)
    return redirect('/')

