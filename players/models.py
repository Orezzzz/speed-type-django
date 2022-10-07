from django.db import models

# Create your models here.

class Players(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    password = models.CharField(max_length=500, null=True)
    score = models.IntegerField(null=True, blank=True, default=False)
