from django.shortcuts import render,redirect
from PEPapp.models import User
from PEPapp.models import Constituency
from django.http import HttpResponse
import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.transaction import TransactionManagementError

# function for homepage view
def home_view(request):
    return render(request, 'PEPapp/home.html')

#Create your views here.
# function for getting data from sigunup form
@csrf_exempt
def get_signup_data(request):
    if request.method=='POST':
        nm=request.POST['user_name']
        em=request.POST['user_email']
        ps=request.POST['user_password']
        mb=request.POST['user_mobile']
        cons=request.POST['user_constituency']
        if  re.compile('[a-zA-Z]*').fullmatch(nm):
            # raise ValidationError('Invalid Name')
            name=nm
        if  re.compile('^[a-z][a-z0-9._%+-]*\@[a-z0-9]*\.[a-z]{2,}').fullmatch(em):
            # raise ValidationError('Invalid email')
            email=em
        if  re.compile('[a-zA-Z1-9@$]*').fullmatch(ps):
            # raise ValidationError('Invalid password')
            passwrd=ps
        if  re.compile('[6-9]\d{9}').fullmatch(mb):
            # raise ValidationError('Invalid mobilenumber')
            mobile=mb
        # get id of the constituency
        const_id = get_object_or_404(Constituency,constituency_name=cons).constituency

        # save the record into users table
        try:
            if not User.objects.filter(uemail=email).exists():
                 reg=User(const_id=const_id,username=name,uemail=email,upassword=passwrd,umobile=mobile,uconsname=cons)
                 regstatus=reg.save()
                 # send HttpResponse
                 responseData = {
                     'code': 200,
                     'message': 'Successfully registered',
                     'data' :{
                        'user_email': email,
                        'username' : name,
                        'constituency_id': const_id,
                        'constituency_name': cons
                     }
                 }
                 return JsonResponse(responseData)
            else:
                # send HttpResponse
                responseData = {
                    'code': 400,
                    'message': 'This Email has already been registered',
                }
                return JsonResponse(responseData)
        except:
            # log the exceptions
            responseData = {
                'code': 500,
                'message': 'Something went wrong!!',
            }
    else:
        return render(request,'PEPapp/signup.html')
