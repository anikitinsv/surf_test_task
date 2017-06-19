from django.db import models

# Create your models here.

class BookAuthor(models.Model):
    first_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)