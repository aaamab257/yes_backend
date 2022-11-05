from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from students.serializer import   UserLoginSerializer,   UserRegistrationSerializer
from django.contrib.auth import authenticate
from students.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import json
from datetime import datetime
from material.models import *
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Student
# Create your views here.


# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(request=self.request ,email=email, password=password)
    token = get_tokens_for_user(user)
    return Response({'code':status.HTTP_200_OK ,'token':token, 'msg':'Login Success' ,
      'user':{'is_admin':user.is_admin , 'tc':user.tc, 'birthdate':user.date_of_birth}})
    print(user)
    # if user is not None:
    #   token = get_tokens_for_user(user)
    #   json_str = json.dumps({user.date_of_birth}, default=str)
    #   return Response({'code':status.HTTP_200_OK ,'token':token, 'msg':'Login Success' ,
    #   'user':{'is_admin':user.is_admin , 'tc':user.tc, 'birthdate':user.date_of_birth}})
    # else:
    #   return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)