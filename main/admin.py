from django.contrib import admin
from .models import Reservation, Residence, Customer, Capacity

admin.site.register(Reservation)
admin.site.register(Residence)
admin.site.register(Customer)
admin.site.register(Capacity)
