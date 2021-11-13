from django.db import models
from django.db.models.deletion import CASCADE

class Farmers(models.Model):
    farmer_name = models.CharField(max_length=250)
    farm_name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.farmer_name

class Staffs(models.Model):
    staff_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.IntegerField()
    department = models.CharField(max_length=250)
    position = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_name


class Records(models.Model):
    farmer_name = models.ForeignKey(Farmers, on_delete=CASCADE)
    title = models.CharField(max_length=250, default='describe the type of tea')
    quantity = models.IntegerField()
    quality = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Payments(models.Model):
    farmer_name = models.ForeignKey(Farmers, on_delete=CASCADE)
    amount = models.IntegerField()
    date_paid = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.farmer_name

