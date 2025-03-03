from django.contrib import admin
from hospitalapp.models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Staff)
admin.site.register(Wards)
admin.site.register(Appointment)
admin.site.register(Contact)
