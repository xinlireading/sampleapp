from django.contrib import admin
from .models import Author, Blog, Entry

# Register your models here.
admin.site.register([Author, Blog, Entry])
