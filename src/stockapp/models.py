from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True , null=True)

    def __str__(self):
        return self.name
    #indexing
    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]
        #indexing

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True , null = True)
    quantity  = models.IntegerField(default=0) 
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    stock = models.IntegerField(default=0) 

    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    null=True,        # allow NULL in database
    blank=True,
    related_name="products"
)
    #indexing
    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["price"]),
        ]
#indexing
# Create your models here.
    def __str__(self):
        return self.name