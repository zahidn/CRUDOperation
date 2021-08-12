from django.db import models


class cruds(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    addess=models.CharField(max_length=100)
    phone=models.IntegerField()
    gender=models.CharField(max_length=1)
    
