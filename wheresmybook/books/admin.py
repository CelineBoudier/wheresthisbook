from django.contrib import admin

# Register your models here.
from .models import Employee, Shelf, Book

admin.site.register(Employee)
admin.site.register(Shelf)
admin.site.register(Book)
