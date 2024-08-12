from django.db import models

# Product Model:
#  id: Integer (auto-increment)
#  name: String
#  description: String
#  price: Float
#  quantity: Integer

class Product(models.Model):
        name = models.CharField(unique=True, max_length=30)
        slug = models.CharField(unique=True, max_length=35, blank=True, null=True)
        description = models.TextField(blank=True, null=True)
        price = models.FloatField()
        quantity = models.IntegerField(default=0)

        def __str__(self):
                return f"{self.name}"
        

