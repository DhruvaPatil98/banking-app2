from apps.netbankingapp.serializer import UsersSerializer, AccountSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from apps.netbankingapp.models import Users
from apps.netbankingapp.utils.utils import AccountNumberGenerator

class UserHelper:

    def create_user(data):
        serialize = UsersSerializer(data=data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data)

        else:
            return JsonResponse(serialize.errors)

    def list_user():
        users = Users.objects.all()
        return Response(UsersSerializer(users, many=True).data)

    def user_details(pk):
        selectedUser = Users.objects.get(pk=pk)
        return Response(UsersSerializer(selectedUser).data)

    def delete_user(pk):
        selectedUser = Users.objects.get(pk=pk)
        Username = selectedUser.username
        selectedUser.delete()
        return Response(Username + " deleted", status=status.HTTP_204_NO_CONTENT)


class AccountHelper:

    def create_account(pk, pin):
        accountdata = {
            'user': Users.objects.get(pk=pk).pk,
            'account_no': AccountNumberGenerator(),
            "pin": pin['pin'],
            'balance': 2000.00
        }

        serialize = AccountSerializer(data=accountdata)
        if serialize.is_valid():
            serialize.save()
            return Response("Account Created")
        else:
            return Response(serialize.errors)

    def list_account(pk):
        accounts = Users.objects.get(pk=pk).accounts.all()
        return Response(AccountSerializer(accounts, many=True).data, status=status.HTTP_200_OK)
