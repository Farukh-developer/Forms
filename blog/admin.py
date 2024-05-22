from django.contrib import admin
from .models import Adminstrator, Students 
# Register your models here.
admin.site.register([Adminstrator, Students])
