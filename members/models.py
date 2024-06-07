from django.db import models
from datetime import date
# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225)
    phone_num = models.CharField(max_length=20,null=True,unique=True)
    date_inserted = models.DateField(null=False, blank=False, default=date.today)
    user_name = models.CharField(max_length=225,unique=True)
    password = models.CharField(max_length=225, blank=False)
    profile = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
