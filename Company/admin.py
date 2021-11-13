from django.contrib import admin
from .models import Farmers, Staffs, Payments, Records

admin.site.register(Farmers)
admin.site.register(Staffs)
admin.site.register(Payments)
admin.site.register(Records)