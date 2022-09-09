from django.urls import path
from dentist.views import signup,home,galeria,venners,invisalign,ortodonci,zbardhimi,contact,rezervo,pricing

urlpatterns=[
    path('',home,name='home'),
    path('galeria/',galeria,name='galeria'),
    path('venners/',venners,name='venners'),
    path('invisalign/',invisalign,name='invisalign'),
    path('ortodonci/',ortodonci,name='ortodonci'),
    path('zbardhimi/',zbardhimi,name='zbardhimi'),
    path('contact/',contact,name='contact'),
    path('rezervo/',rezervo,name='rezervo'),
    path('pricing/',pricing,name='pricing'),
    path('signup/',signup,name='signup')

]
