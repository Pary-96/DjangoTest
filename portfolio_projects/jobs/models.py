from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=200)


class CRUD(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3, null=True)
    designation = models.TextField(max_length=256, null=True)
