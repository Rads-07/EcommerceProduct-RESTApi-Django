from django.db import models

class Product(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None','None'),
    )

    #product_id = models.IntegerField()
    product_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=10000, null=True)
    category = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200,null=True)
    size = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=10, null=True, choices =GENDER)
    price = models.FloatField(null=True)
    image = models.URLField(max_length=10000)


    def __str__(self):
        return self.product_name
