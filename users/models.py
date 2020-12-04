from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField('biographie')
    phone=models.CharField(max_length=50 ,blank=True , null=True)
    created=models.DateTimeField()
    birth_date=models.DateTimeField('date de naissance')
    town=models.CharField(max_length=250, null=True, blank=True )
    sex=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photos/%Y/%m/%d/', default='media/default.png')

    def __str__(self):
        return self.user



