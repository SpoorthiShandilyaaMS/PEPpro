from django.contrib import admin
from PEPapp.models import Constituency,User,News_Feed,Sector,Complaint,Query,Answer

# Register your models here.
@admin.register(Constituency)
class ConstituencyAdmin(admin.ModelAdmin):
    list_display=['constituency','constituency_name','constituency_description']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','uemail','upassword','umobile','uconsname']


@admin.register(News_Feed)
class UserAdmin(admin.ModelAdmin):
    list_display=['feed_title','feed_description','feed_date','constituency_name','constituency']


@admin.register(Sector)
class UserAdmin(admin.ModelAdmin):
    list_display=['sector_id','sector_name','sector_scope']


@admin.register(Complaint)
class UserAdmin(admin.ModelAdmin):
    list_display=['complaint_id','complaint_subject','complaint_details','posted_by','constituency_id','no_up_vote','sector_name','upvoted_by']


@admin.register(Query)
class UserAdmin(admin.ModelAdmin):
    list_display=['query_id','query','posted_by','date']



@admin.register(Answer)
class UserAdmin(admin.ModelAdmin):
    list_display=['answer_id','answer','query_id','user_email','date']
