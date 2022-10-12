from django.contrib import admin
from TestApp.models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=["cid","cname","Accno","bank","branch"]


admin.site.register(Customer,CustomerAdmin)
