from rest_framework import serializers
from apps.netbankingapp.models import Users, Account
from datetime import datetime
from django.core.validators import RegexValidator
import re

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'dob',
            'address',
            'password'
        ]

    def validate_first_name(self, first_name):
        if first_name == '':
            raise serializers.ValidationError("First Name cannot be Null or blank..")

        return first_name

    def validate_last_name(self, last_name):
        if last_name == '':
            raise serializers.ValidationError("Last Name cannot be Null or blank..")

        return last_name

    def validate_username(self , username):
        if username == "":
            raise serializers.ValidationError(" Unique Username needed boss..")

        else:
            validators = [
                RegexValidator(
                    r'^[\w.@+-]+$',
                    ('Enter a valid username. '
                        'This value may contain only letters, numbers '
                        'and @/./+/-/_ characters.'), 'invalid'),
            ],
            error_messages = {
                'unique': "A user with that username already exists.",
            }
        return username

    def validate_dob(self, dob):
        today = datetime.now().date()
        diff = today - dob

        if dob > today:
            raise serializers.ValidationError("Give date is in future...")
        else:
            age = diff.days / 365
            if (age < 18):
                raise serializers.ValidationError("You are no eligible to have a bank account..so cannot create user account ")
        return dob

    def validate_password(self , password):
        if password == "":
            raise serializers.ValidationError("Enter password ")

        else:
            if (len(password) < 8):
                raise serializers.ValidationError("Password length must be minimum 8 characters")

            elif not re.search("[a-z]", password):
                raise serializers.ValidationError("password should contain atleatone lowercase letters")

            elif not re.search("[A-Z]", password):
                raise serializers.ValidationError(" password must contain atleast one UpperCase letter")

            elif not re.search("[0-9]", password):
                raise serializers.ValidationError(" password must contain atleast one digit [0 - 9]")

            elif not re.search("[_@$^&*!#]", password):
                raise serializers.ValidationError(" password must contain atleast one special character ")

        return password

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


    def validate_pin(self , pin):
        if pin == "":
            raise serializers.ValidationError("Enter pin (Pin must only contain numbers) ")

        else:
            if int(len(str(pin))) <= 3:
                raise serializers.ValidationError("Pin length must be minimum 4 digits")

        return pin
