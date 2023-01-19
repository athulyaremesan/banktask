from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class AccountType(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=124)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=124)
    phoneno=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    account = models.ForeignKey(AccountType, on_delete=models.SET_NULL, blank=True, null=True)
    is_chequebook = models.BooleanField("Cheque Book", default=False)
    is_creditcard = models.BooleanField("Credit Card", default=False)
    is_debitcard = models.BooleanField("Debit Card", default=False)

    def __str__(self):
        return self.name