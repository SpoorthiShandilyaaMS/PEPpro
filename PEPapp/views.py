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
from django.contrib.auth.models import auth
from django.contrib import messages
from django.core import serializers
from django.forms.models import model_to_dict
import json

# function for homepage view
def home_view(request):
    return render(request, 'PEPapp/home.html')


#csrf_exempt

# function for getting data from sigunup form
@csrf_exempt
def get_signup_data(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        pwd = request.POST.get('user_password')
        mobile = request.POST.get('user_mobile')
        constituency =request.POST.get('user_constituency')

        if(name and email and pwd and constituency):

            # get id of the constituency
            const_id = get_object_or_404(Constituency,constituency_name=constituency).constituency

            # save the record into users table
            try:
                if not User.objects.filter(uemail=email).exists():
                     reg = User(const_id=const_id,username=name,uemail=email,upassword=pwd,umobile=mobile,uconsname=constituency,usertype='public')
                     regstatus = reg.save()
                     # send HttpResponse
                     responseData = {
                         'code': 200,
                         'message': 'Successfully registered',
                         'data' :{
                            'user_email': email,
                            'user_name' : name,
                            'constituency_id': const_id,
                            'constituency_name': constituency
                         }
                     }
                     # return redirect('login')
                     return JsonResponse(responseData)
                else:
                    # send HttpResponse
                    responseData = {
                        'code': 400,
                        'message': 'This Email has already been registered',
                    }
                    return JsonResponse(responseData)
            except Exception as e:
                # log the exceptions
                responseData = {
                    'code': 500,
                    'message': 'Something went wrong!!'+str(e),
                }
                return JsonResponse(responseData)
        else:
            responseData = {
                'code': 400,
                'message': 'No input field can be empty!!!!',
            }
            return JsonResponse(responseData)

    else:
        return render(request,'PEPapp/signup.html')



# function for validating data from login form
@csrf_exempt
def login(request):
    if request.method =='POST':
        email = request.POST.get('user_email')
        pwd = request.POST.get('user_password')

        # if email and pwd not null
        if(email and pwd):
            #if user email exists
            try:
                if User.objects.filter(uemail=email).exists():
                    # if useremail exists and the password matches
                    if User.objects.filter(uemail=email).filter(upassword=pwd).exists():
                        userData = User.objects.filter(uemail=email).values('uemail','uconsname','const_id','username','usertype')
                        responseData={
                            'code': 200,
                            'message': 'login Successful',
                            'user_Data' : list(userData),
                        }
                    else:
                        responseData = {
                            'code': 400,
                            'message': 'Incorrect Password',
                        }
                else:
                    responseData = {
                        'code': 400,
                        'message': 'No user with '+email+' exists.Check email entered!!',
                    }
                return JsonResponse(responseData, safe=False)
            except:
                # log the exceptions
                responseData = {
                    'code': 500,
                    'message': 'Something went wrong!!',
                }
                return JsonResponse(responseData, safe=False)
        else:
            responseData = {
                'code': 400,
                'message': 'Enter proper credentials!!',
            }
        return JsonResponse(responseData, safe=False)

    else:
        return render(request,'PEPapp/login.html')
