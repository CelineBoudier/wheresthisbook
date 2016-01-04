import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
    
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sso_login = models.CharField(max_length=200) #emailfield instead??#

    def __unicode__(self):
        return self.sso_login

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

    class Meta:
        verbose_name_plural = "shelves"
    
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    borrower = models.ForeignKey(Employee, blank=True, null=True)
    borrowed_date = models.DateTimeField('date borrowed', blank=True, null=True)
    shelf = models.ForeignKey(Shelf, blank=True, null=True)

    def __unicode__(self):
        return self.book_name

    def was_borrowed_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.borrowed_date <= now

    def save(self, *args, **kwargs):
        if self.borrower:
            if not self.borrowed_date:
                print ("please provide a date")
                return
        elif not self.shelf:
            print ("please provide either a shelf or a borrower")
            return
        super(Book, self).save(*args, **kwargs)
