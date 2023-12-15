import uuid
from django.db import models

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=50)
    blood_group= models.CharField(max_length=5)
    mobile_no= models.IntegerField()
    address= models.CharField(max_length=500)