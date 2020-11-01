from django.db import models

# Create your models here.
class Constituency(models.Model):
    constituency=models.IntegerField(primary_key=True,default=100)
    constituency_name=models.CharField(max_length=20)
    constituency_description=models.CharField(max_length=200)
class User(models.Model):
    const=models.ForeignKey(Constituency,on_delete=models.CASCADE)
    username=models.CharField(max_length=20,null=False)
    uemail=models.EmailField(primary_key=True,null=False)
    upassword=models.CharField(max_length=20,null=False)
    umobile=models.IntegerField(null=False)
    uconsname=models.CharField(max_length=20,default='basavangudi')
