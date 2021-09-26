from django.contrib import admin
from django.contrib.auth import models
from .models import *

# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)