from django.contrib import admin
from PEPapp.models import Constituency,User

# Register your models here.
@admin.register(Constituency)
class ConstituencyAdmin(admin.ModelAdmin):
    list_display=['constituency','constituency_name','constituency_description']
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','uemail','upassword','umobile','uconsname']
