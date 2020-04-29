from django.shortcuts import render
from .models import Image

# Create your views here.
def home(request):
    print(request.user.username)
    return render(request, 'home.html')

def services(request):
    return render(request,'PortFolio.html')

def image(request):

    Img = Image.objects.all()
    return render(request,'Image.html',{'Img': Img})

def add(request):
    val1= int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    result = val1+val2
    return render(request,'result.html',{'result':result})

def contact(request):
    return render(request,'contact.html')