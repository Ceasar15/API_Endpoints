from django.db import models

# Create your models here.


class Tutorial(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=250, blank=False, default='')
    published = models.BooleanField(default=False)