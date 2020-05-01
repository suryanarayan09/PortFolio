from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User, auth

# Create your views here.
def information(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        if subject == 'Save':
            providing_field = request.POST['providingfield']
            sub_field = request.POST['subfield']
            users = request.user
            specificuser = ServiceBox(user=users, providing_field=providing_field, sub_field=sub_field)
            specificuser.save()
            return redirect('/')
        else:
            providing_field = request.POST['providingfield']
            sub_field = request.POST['subfield']
            users = request.user
            specificuser = ServiceBox(user=users, providing_field=providing_field, sub_field=sub_field)
            specificuser.save()
            return render(request,'user_file.html')
    else:
        return render(request,'user_file.html')


def dashboard(request):
    if request.user.is_authenticated:
        todo_list = ServiceBox.objects.filter(user=request.user)
        return render(request, 'customer.html',{'todo_list':todo_list})
    else:
        return redirect('/')