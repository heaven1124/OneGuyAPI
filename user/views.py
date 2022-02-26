from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework import serializers, viewsets

from user.models import AppUser

from .models import AppUser

# Create your views here.


# 序列化类
class UserModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'name', 'phone')


# api视图类
class UserAPIView(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserModelSerializer


class UserApi(View):
    def get(self, request):
        user_all = AppUser.objects.all()
        ser = UserModelSerializer(user_all, many=False)

        return JsonResponse({
            'data': ser.data
        })



