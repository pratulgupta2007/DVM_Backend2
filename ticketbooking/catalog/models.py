from django.db import models
from django.urls import reverse
import uuid

class wallet(models.Model):
    walletid=models.UUIDField(default=uuid.uuid4, primary_key=True)
    balance=models.DecimalField(max_digits=10, decimal_places=2)
    transaction=models.BinaryField(max_length=2000)

class transactions(models.Model):
    transactionsID=models.UUIDField(default=uuid.uuid4, primary_key=True)
    sendingID=models.ForeignKey(wallet, on_delete=models.CASCADE, related_name="sender")
    receivingID=models.ForeignKey(wallet, on_delete=models.CASCADE, related_name="receiver")
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=1,
                            choices={
                                "I": "Incomplete",
                                "R": "Reverted",
                                "C": "Completed"
                            }, default="I")


class user(models.Model):
    uid=models.UUIDField(default=uuid.uuid4, primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    walletid=models.ForeignKey(wallet, on_delete=models.CASCADE)
    shows=models.BinaryField(max_length=2000)
    food=models.BinaryField(max_length=2000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user-info', args=[str(self.uid)])


class adminuser(models.Model):
    aid=models.UUIDField(default=uuid.uuid4, primary_key=True)
    password=models.CharField(max_length=200)
    verification_email=models.EmailField()
    walletid=models.ForeignKey(wallet, on_delete=models.CASCADE)

    #Theater related information
    theater_name=models.CharField(max_length=200)
    theater_address=models.CharField(max_length=200)
    theater_phone=models.CharField(max_length=13)
    theater_email=models.EmailField()
    revenue=models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.theater_name
    

    def get_absolute_url(self):
        return reverse('admin-info', args=[str(self.aid)])


class shows(models.Model):
    showID=models.UUIDField(default=uuid.uuid4, primary_key=True)
    adminID=models.ForeignKey(adminuser, on_delete=models.CASCADE)
    movie=models.CharField(max_length=255, help_text="Enter a movie name: ")
    language=models.CharField(max_length=20, help_text="Enter movie language: ")
    date_time=models.DateTimeField()
    duration=models.DurationField()
    seats=models.BinaryField(max_length=2000)

    def __str__(self):
        return self.movie

    def get_absolute_url(self):
        return reverse('show', args=[str(self.showID)])

class foods(models.Model):
    foodID=models.CharField(max_length=20, primary_key=True)
    adminID=models.ForeignKey(adminuser, on_delete=models.CASCADE)
    itemname=models.CharField(max_length=255, help_text="Enter item name: ")
    price=models.DecimalField(max_digits=5, decimal_places=2, help_text="Enter item price: ")
    availibilty=models.BooleanField()

    def __str__(self):
        return self.itemname

    def get_absolute_url(self):
        return reverse('show', args=[str(self.foodID)])