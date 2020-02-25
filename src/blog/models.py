from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=25,blank=True)
    desc = models.TextField(default="season description in few lines")