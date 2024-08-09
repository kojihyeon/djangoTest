from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    password = models.CharField(max_length=20, default=None, null=True)
    image = models.CharField(max_length=500, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=200)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) # CASCADE - 이 레스토랑이 삭제되었을 때 리뷰도 삭제

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)