from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from read.Serializers import UserSerializer
from read.models import User
import json


class UserOperations(APIView):
    # fetch data
    def get(self, request):
        list = [{'uid': 1, 'name': 'vinay'}, {'uid': 2, 'name': 'ajay'}, {'uid': 3, 'name': 'vijay'}]
        data = json.dumps(list)
        Users = User.objects.all()
        serializer = UserSerializer(Users, many=True)
        return Response(serializer.data)

    # add data
    @csrf_exempt
    def post(self, request):
        print("aya post mai")
        serial = UserSerializer(data=request.data)
        # print(serial.data)
        if serial.is_valid():
            serial.save()
            return Response(True, status=status.HTTP_201_CREATED)
        print(serial.data)
        print("post")
        return Response("User already exists", status=status.HTTP_400_BAD_REQUEST)

    # update data
    @csrf_exempt
    def put(self, request):
        serial = UserSerializer(data=request.data)
        if not serial.is_valid():
            try:
                t = User.objects.get(uid=int(serial.data['uid']))
                t.Name = serial.data['Name']
                t.email = serial.data['email']
                t.password = serial.data['password']
                t.save()
                # return Response(serial.data, status=status.HTTP_202_ACCEPTED)
                return Response(True, status=status.HTTP_202_ACCEPTED)
            except User.DoesNotExist:
                # return Response("User doesn't exists", status=status.HTTP_400_BAD_REQUEST)
                return Response(False, status=status.HTTP_400_BAD_REQUEST)
        else:
            # return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(False, status=status.HTTP_400_BAD_REQUEST)
    # delete data
    @csrf_exempt
    def delete(self, request):
        serial = UserSerializer(data=request.data)
        if not serial.is_valid():
            print("delete")
            UID = serial.data['uid']
            print(UID)
            instance = User.objects.filter(uid=UID)
            if instance.exists():
                print("delete")
                instance.delete()
                return Response(serial.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        print("delete not valid")
        return Response("User doesn't exists", status=status.HTTP_400_BAD_REQUEST)
