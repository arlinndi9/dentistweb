import datetime

from django.db import models
from django.contrib.auth.models import User


class Mendimi(models.Model):
    description=models.TextField()
    name=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255,default=' ')

    def __str__(self):
        return self.name

class Galeria(models.Model):
    before=models.ImageField(upload_to='images/')
    description=models.CharField(max_length=255,default='pershkrimi' )
# Create your models here.

class Veneers(models.Model):
    titulli=models.CharField(max_length=255,default='Venners')
    descriptioN=models.TextField()
    foto=models.ImageField(upload_to='images/')

class Invisalign(models.Model):
    titulli=models.CharField(max_length=255,default='Invisalign')
    descriptioN=models.TextField()
    foto=models.ImageField(upload_to='images/')

class Ortodonci(models.Model):
    titulli = models.CharField(max_length=255, default='Ortodonci')
    descriptioN = models.TextField()
    foto = models.ImageField(upload_to='images/')

class Zbardhimi(models.Model):
    titulli = models.CharField(max_length=255, default='Zbardhimi I Dhembeve')
    descriptioN = models.TextField()
    foto = models.ImageField(upload_to='images/')

class Contact(models.Model):
    name=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    subject=models.TextField()
    def __str__(self):
        return self.name

class Rezervo(models.Model):
    #customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    #nuk kemi nevoje me caktu field per id sepse django gjeneron id automatikisht
    #decimalfield e perdorim per qmime spse eshte me i sakte
    name = models.CharField("Name",max_length=255)
    lastname = models.CharField("Lastname",max_length=255)
    phonenumber=models.IntegerField(

    )
    email=models.EmailField("Email",max_length=255)
    addresa=models.CharField("Address",max_length=255,null=True,blank=True)
    #listoftuple e perdorim nese kem me ndryshu najnjanen prej tuples
    zgjedh_sherbimin = (
        ('Heqja e një shtrese të vjetër, kurorë e vjetër', 'Heqja e një shtrese të vjetër, kurorë e vjetër'),
        ('Kurorë standarde prej porcelani dhe zirkoni në implant', 'Kurorë standarde prej porcelani dhe zirkoni në implant'),
        ('Implantimi i një implanti (çmimi varet nga sistemi i përdorur)', 'Implantimi i një implanti (çmimi varet nga sistemi i përdorur)'),
        ('Mbulimi i recesionit të mishrave të dhëmbëve', 'Mbulimi i recesionit të mishrave të dhëmbëve'),
        ('Kurora dhe mbushje qeramike Porcelani dentar','Kurora dhe mbushje qeramike Porcelani dentar'),
        ('Shërbimi i zbardhjes së dhëmbëve në Klinikën Dentare','Shërbimi i zbardhjes së dhëmbëve në Klinikën Dentare'),
        ('Zbardhja e dhëmbëve me mbulesë (2 harqe)','Zbardhja e dhëmbëve me mbulesë (2 harqe)')
    )
    sherbimi=models.CharField(max_length=255,choices=zgjedh_sherbimin)
    date=models.DateField("Purchase Date(year/mm/day)",default='2022-1-1')
    message=models.TextField()
    def __str__(self):
        return self.name

class Pricing(models.Model):
    servicesname=models.CharField("Services Name",max_length=255)
    stage=models.CharField("Stage",max_length=255,default="1 times")
    price=models.IntegerField("Price")

    def __str__(self):
        return self.servicesname


