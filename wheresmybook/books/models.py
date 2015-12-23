from django.db import models

# Create your models here.
    
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sso_login = models.CharField(max_length=200) #emailfield instead??#

class Shelf(models.Model):
    BUILDING_CHOICES=(
        ('TI', 'Titan Court'),
        ('AP', 'Apollo Court'),
    )
    FLOOR_CHOICES=(
        ('G', 'Ground Floor'),
        ('1', 'First Floor'),
        ('2', 'Second Floor'),
        ('3', 'Third Floor'),
    )
    building = models.CharField(max_length=2, choices=BUILDING_CHOICES)
    floor = models.CharField(max_length=1, choices=FLOOR_CHOICES)
    room = models.CharField(max_length=100)
    shelf_url = models.URLField(max_length=200)
    coordinate_x = models.IntegerField() #coords on the picture
    coordinate_y = models.IntegerField()
    
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    image_url = models.URLField(max_length=200)
    borrower = models.ForeignKey(Employee)
    borrowed_date = models.DateTimeField('date borrowed')
    shelf = models.ForeignKey(Shelf)
