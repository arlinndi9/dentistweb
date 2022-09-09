
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Contact,Rezervo
from dentist.models import Mendimi
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dentist.models import Mendimi,Galeria,Veneers,Invisalign,Ortodonci,Zbardhimi,Pricing
# Create your views here.
def home(request):
    u=User.objects.all()
    mendimi=Mendimi.objects.all().order_by('id').values()
    data={
        'mendim':mendimi,
        'u':u
    }
    return render(request,'home.html',data)

def galeria(request):
    galeri=Galeria.objects.all()
    data={
        'galeri':galeri
    }
    return render(request,'galeria.html',data)

def venners(request):
    venners=Veneers.objects.all()
    data={
        'venners':venners
    }
    return render(request,'venners.html',data)

def invisalign(request):
    invisalign=Invisalign.objects.all()
    data={
        'invisalign':invisalign
    }
    return render(request,'invisalign.html',data)

def ortodonci(request):
    ortodonci=Ortodonci.objects.all()
    data={
        'ortodonci':ortodonci
    }
    return render(request,'ortodonci.html',data)

def zbardhimi(request):
    zbardhimi=Zbardhimi.objects.all()
    data={
        'zbardhimi':zbardhimi
    }
    return render(request,'zbardhimi.html',data)

def pricing(request):
    price=Pricing.objects.all()
    data={
        'price':price
    }
    return render(request,'price.html',data)
def contact(request):
    if request.method=="POST":
        form=Contact(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request,'contact.html',{'form':Contact})

def rezervo(request):
    if request.method=="POST":
       form=Rezervo(request.POST)
       if form.is_valid():
           form.save()
       return redirect('home')
    return render(request,'rezervo.html',{'form':Rezervo})

def signup(request):
    if request.method== 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})