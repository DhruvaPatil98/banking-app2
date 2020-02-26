from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from apps.netbankingapp.services.service import UserHelper

# Create your views here.
def home(request):
    return HttpResponse("HomePage")


class UserViewSet(viewsets.ViewSet):

    def create_user(self, request):
        return UserHelper.create_user(request.data)

    def list_user(self , request):
        return UserHelper.list_user()
