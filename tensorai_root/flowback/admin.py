# Register your models here.
from django.contrib import admin

from .models import Well_Profile, Well_Data, Well_Data_Calc

admin.site.register(Well_Profile)
admin.site.register(Well_Data, Well_Data_Calc)