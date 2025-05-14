from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(primary_key=True)
    roll=models.IntegerField()
    city=models.CharField()

    def __str__(self):
        return self.name
    

class players(models.Model):
    jer_no=models.CharField(primary_key=True)
    pname=models.CharField()
    role=models.CharField()
    team=models.CharField()

    def __str__(self):
        return self.pname
    




