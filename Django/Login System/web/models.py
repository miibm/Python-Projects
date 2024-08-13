from django.db import models

# Create your models here.

class userModel(models.Model):
    username = models.CharField(max_length=255)
    email    = models.CharField(max_length=255,blank=True,null=True)
    phno     = models.CharField(max_length=255,blank=True,null=True)
    age      = models.IntegerField(blank=True,null=True)
    gender   = models.CharField(max_length=255,blank=True,null=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username