from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.category

    category = models.CharField(max_length=256)

class Drink(models.Model):
    class Meta:
        db_table = "drinks"

    def __str__(self):
        return self.drink_name

    drink_name = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    menu = models.ManyToManyField(Category)


