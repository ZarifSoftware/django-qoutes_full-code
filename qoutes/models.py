from django.db import models

class Bangla(models.Model):
    author = models.CharField(max_length=300)
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=3000)

class English(models.Model):
    author = models.CharField(max_length=300)
    title = models.CharField(max_length=30)
    text = models.TextField()   
