from apps.netbankingapp.serializer import UsersSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from apps.netbankingapp.models import Users


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
