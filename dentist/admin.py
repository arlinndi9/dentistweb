from django.contrib import admin
from .models import Mendimi,Contact,Rezervo,Pricing
# Register your models here.
admin.site.register(Mendimi)
admin.site.site_header='Dentist App'
admin.site.index_title=' '

@admin.register(Rezervo)
class RezervoAdmin(admin.ModelAdmin):
    list_display = ['name','lastname','sherbimi','date']
    list_editable = ['sherbimi','date']
    list_per_page = 10

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ['servicesname','stage','price']
    list_editable = ['price']
    ordering = ['servicesname']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =['name','lastname','subject']
