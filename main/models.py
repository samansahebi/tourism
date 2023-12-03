from django.db import models


class Capacity(models.Model):
    baby = models.IntegerField()
    child = models.IntegerField()
    adult = models.IntegerField()


class Residence(models.Model):
    title = models.CharField(max_length=50)
    capacity = models.ForeignKey(Capacity, on_delete=models.CASCADE)
    is_vacant = models.BooleanField(default=True)
    price = models.BigIntegerField()
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    national_id = models.CharField(max_length=11)


class Reservation(models.Model):
    residence = models.ForeignKey(Residence, on_delete=models.PROTECT)
    reservation_start_date = models.DateTimeField()
    reservation_end_date = models.DateTimeField()
    customers = models.ManyToManyField(Customer)
