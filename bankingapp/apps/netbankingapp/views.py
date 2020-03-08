from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from apps.netbankingapp.services.service import UserHelper, AccountHelper, TransactionHelper


# Create your views here.
def home(request):
    return HttpResponse("HomePage")


class UserViewSet(viewsets.ViewSet):

    def create_user(self, request):
        return UserHelper.create_user(request.data)

    def list_user(self, request):
        return UserHelper.list_user()

    def user_details(self, request, pk):
        return UserHelper.user_details(pk)

    def delete_user(self, request, pk):
        return UserHelper.delete_user(pk)

class AccountViewSet(viewsets.ViewSet):

    def create_account(self, request, pk):
        return AccountHelper.create_account(pk, request.data)

    def list_accounts(self, request, pk):
        return AccountHelper.list_account(pk)

    def bank_action(self, request, pk, account_id):
        state = str(request.data['action'])
        money = int(request.data['money'])

        if state == 'w' or state == 'd':
            return TransactionHelper.action(pk, account_id, money, state)
        else:
            return Response("Invalid action ..")

class TransactionViewSet(viewsets.ViewSet):

    def list_transactions(self, request, pk):
        return TransactionHelper.list_transactions()
