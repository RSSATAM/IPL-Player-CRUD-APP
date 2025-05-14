from django.contrib import admin
from App1.models  import student
from .models import players

# Register your models here.

admin.site.register(student)
admin.site.register(players)
