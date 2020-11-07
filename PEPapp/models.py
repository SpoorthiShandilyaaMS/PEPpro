from django.db import models
from django.utils import timezone
import pytz

# Create your models here.
class Constituency(models.Model):
    constituency=models.IntegerField(primary_key=True,default=100)
    constituency_name=models.CharField(max_length=20)
    constituency_description=models.CharField(max_length=1500)
    # file=models.FileField(null=True)



class User(models.Model):
    const=models.ForeignKey(Constituency,on_delete=models.CASCADE)
    username=models.CharField(max_length=20,null=False)
    uemail=models.EmailField(primary_key=True,null=False)
    upassword=models.CharField(max_length=20,null=False)
    umobile=models.CharField(max_length=10,null=True,blank=True)
    uconsname=models.CharField(max_length=20,default='basavangudi')
    usertype=models.CharField(max_length=10,null=True)



class News_Feed(models.Model):
    # feed_id=models.IntegerField(primary_key=True)
    feed_title=models.CharField(max_length=50,null=False)
    feed_description=models.CharField(max_length=400,null=False)
    feed_date=models.DateTimeField(auto_now=True,null=True,blank=True)
    constituency_name=models.CharField(max_length=20,null=False)
    constituency=models.ForeignKey(Constituency,on_delete=models.CASCADE)



class Sector(models.Model):
    sector_id=models.IntegerField(primary_key=True)
    sector_name=models.CharField(max_length=20)
    sector_scope=models.CharField(max_length=300)



class Complaint(models.Model):
    complaint_id=models.IntegerField(primary_key=True)
    complaint_subject=models.CharField(max_length=50,null=False)
    complaint_details=models.CharField(max_length=300,null=False)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    constituency_id=models.ForeignKey(Constituency,on_delete=models.CASCADE)
    no_up_vote=models.IntegerField(null=False)
    sector_name=models.ForeignKey(Sector,on_delete=models.CASCADE)
    upvoted_by=models.CharField(max_length=50,null=True)



class Query(models.Model):
    query_id = models.IntegerField(primary_key=True)
    query=models.CharField(max_length=100,null=False)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)



class Answer(models.Model):
    answer_id=models.IntegerField(primary_key=True)
    answer=models.CharField(max_length=200,null=False)
    query_id=models.ForeignKey(Query,on_delete=models.CASCADE)
    user_email=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
