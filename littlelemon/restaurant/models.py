from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.FloatField()
    Inventory = models.IntegerField()
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
