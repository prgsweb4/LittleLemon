from django.db import models


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200, default='') 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 
   inventory = models.SmallIntegerField(default=0)

   def __str__(self):
      return self.name
  
# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255, default='') 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField(default=0)
    def get_item(self):
        return f'{self.name} : {str(self.price)}'