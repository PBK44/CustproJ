from django.shortcuts import render
from TestApp.models import Customer
# Create your views here.
def homeview(request):
    return render(request,"TestApp/home.html")

def custview(request):
    cust_list=Customer.objects.all()
    my_dict={'cust_list':cust_list}
    return render(request,"TestApp/cust.html",context=my_dict)  
