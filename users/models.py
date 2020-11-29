from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField('biographie')
    phone=models.IntegerField()
    created=models.DateTimeField()
    birth_date=models.DateTimeField('date de naissance')
    town=models.CharField(max_length=250)
    sex=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.user


# Create your models here.
