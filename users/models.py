from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.






# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE) 
#     bio = models.CharField(max_length=30)
#     age = models.IntegerField(null=True, blank=True)
#     location = models.CharField(max_length=40)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()   


