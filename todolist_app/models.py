from django.db import models

# Create your models here.

class Details(models.Model):
    firstName = models.CharField(max_length = 150 )
    lastName = models.CharField(max_length=150)
    emailAddress = models.EmailField(max_length = 150 )
    displayName = models.CharField(max_length = 20 )
    homePhone = models.CharField(max_length = 15 )


# from django.contrib.auth.models import User
#
# class UserProfile(models.Model):
#     user   = models.OneToOneField(User)
#     avatar = models.ImageField()
