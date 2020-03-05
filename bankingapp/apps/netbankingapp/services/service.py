from apps.netbankingapp.serializer import (
    UsersSerializer,
    AccountSerializer,
    TransactionSerializer,
)
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from apps.netbankingapp.models import Users, Account, AllTransactions
from apps.netbankingapp.utils.utils import AccountNumberGenerator
from django.db.models import F


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

class TransactionHelper:

    def withdraw(pk, account_id, money):
        account = Account.objects.get(pk=account_id)
        if float(money) > account.balance:
            return Response(" Unsufficient balance ")
        elif account.balance <= 2000:
            return Response(" Cannot withdraw money...Account balance less than mininum balance")
        elif account.balance - money <= 2000:
            return Response(" Withdrawing this amount cause balance to go below minimum balance ..So cannot withdraw")
        else:

            data = {
                "withdrawstatus": money,
                "account": account.pk
            }

            account.balance = F('balance') - money
            account.save()

            serializedata = TransactionSerializer(data=data)
            if serializedata.is_valid():
                log_file = open("log.txt", "a+")
                log_file.write(str(serializedata.validated_data))
                log_file.write("\n")
                log_file.close()
                serializedata.save()
                return Response(serializedata.data)
            else:
                return Response(serializedata.errors)

    def deposit(pk, account_id, money):
        account = Account.objects.get(pk=account_id)
        data = {
            "depositstatus": money,
            "account": account.pk
        }

        account.balance = F('balance') + money
        account.save()

        serializedata = TransactionSerializer(data=data)
        if serializedata.is_valid():
            log_file = open("log.txt", "a+")
            log_file.write(str(serializedata.validated_data))
            log_file.write("\n")
            log_file.close()
            serializedata.save()
            return Response(serializedata.data)
        else:
            return Response(serializedata.errors)


    def action(pk, account_id, money, state):
        if state == 'w':
            return TransactionHelper.withdraw(pk, account_id, money)

        if state == 'd':
            return TransactionHelper.deposit(pk, account_id, money)

    def list_transactions():
        transactions = AllTransactions.objects.all()
        query_set = TransactionSerializer(transactions, many=True)
        return Response(query_set.data)
