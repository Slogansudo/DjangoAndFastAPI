from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Address(models.Model):
    name = models.CharField(max_length=50, null=False)
    loking_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Mete:
        db_table = "address"

    def __str__(self):
        return self.name


class Places(models.Model):
    name = models.CharField(max_length=50, null=False)
    rating = models.IntegerField(default=0)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Mete:
        db_table = "places"

    def __str__(self):
        return self.name


class TravelCategory(models.Model):
    name = models.CharField(max_length=50, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Mete:
        db_table = "travel_category"

    def __str__(self):
        return self.name


class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reads_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Mete:
        db_table = "comments"

    def __str__(self):
        return self.text[:10]


class PriceType(models.TextChoices):
    sum = "sum", "SUM"
    usd = "$", "$"


class Travels(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField()
    price_type = models.CharField(max_length=20, choices=PriceType.choices)
    description = models.TextField()
    category = models.ForeignKey(TravelCategory, on_delete=models.CASCADE)
    places = models.ForeignKey(Places, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    discount = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Mete:
        db_table = "travels"

    def __str__(self):
        return self.name
