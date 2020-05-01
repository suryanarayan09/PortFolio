from django.shortcuts import render,redirect
from .models import Image
from UserInfo.models import *

# PortFolio,image,ServiceBox,ShowcaseContent,ShowcaseImage,About,AboutImage
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        Portfolio = PortFolio.objects.filter(user=request.user)
        return render(request,'home.html',{'Portfolio': Portfolio})
    else:
        Portfolio = PortFolio.objects.filter(user=1)
        return render(request, 'home.html',{'Portfolio': Portfolio})

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