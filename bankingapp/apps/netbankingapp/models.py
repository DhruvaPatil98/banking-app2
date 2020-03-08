from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
import uuid

# Create your models here.
class Users(models.Model):

    id = models.UUIDField(
        primary_key=True, unique=True, editable=False,
        default=uuid.uuid4
        )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    username = models.CharField(
        max_length=30, unique=True, null=True, blank=True,
        help_text=(
            'Required. 30 characters or fewer. Letters, digits and '
            'Use special characters in case the given username is repeated'
        ))

    dob = models.DateField(blank=False, null=False)
    address = models.CharField(max_length=100)

    password = models.CharField(
        max_length=300, unique=False, null=True, blank=True,
        help_text=(
              'Required. 30 characters or fewer. Letters, digits and '
              'special characters'
          ))

    def __str__(self):
        return str(self.username)

class Account(models.Model):
    account_id = models.UUIDField(
                                  primary_key=True,
                                  editable=False,
                                  unique=True,
                                  default=uuid.uuid4
                                )
    user = models.ForeignKey(
            Users, on_delete=models.CASCADE, related_name='accounts'
        )

    #using MinValueValidator and MaxValueValidator to validate account number to have 8 digits

    account_no = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(10000000),
            MaxValueValidator(99999999)
        ],
        null=True, blank=True
    )

    #validating password to have special characters and upper and lower case letters and digits
    pin = models.CharField(
         max_length=6,
         unique=False, null=True, blank=True,
         help_text=(
              'Required. 6 digits'
          ))

    balance = models.DecimalField(decimal_places=2, max_digits=15)

    def __str__(self):
        return str(self.account_no) + " balance: " + str(self.balance)


class AllTransactions(models.Model):
    time = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(
            Account, on_delete=models.CASCADE, related_name="account"
        )
    receiveracc = models.ForeignKey(
            Account, on_delete=models.CASCADE,
            null=True, blank=True, related_name="receiversacc"
        )
    withdrawstatus = models.DecimalField(
            decimal_places=2, max_digits=15, null=True, blank=True
        )
    depositstatus = models.DecimalField(
            decimal_places=2, max_digits=15, null=True, blank=True
        )
    transferedMoney = models.DecimalField(
            decimal_places=2, max_digits=15, null=True, blank=True
        )
