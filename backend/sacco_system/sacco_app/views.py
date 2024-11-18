from django.http import HttpResponse
from django.shortcuts import render

from sacco_app.models import Customer


# Create your views here.
def test(request):
    # c1= Customer(first_name="Saida",last_name="Ali" ,email="saida@gmail.com",dob="2004-4-05",gender="female",weight="58")
    # c1.save()
    #
    # c2 = Customer(first_name="Flex", last_name="Kash", email="flex@gmail.com", dob="2006-4-05", gender="male",
    #               weight="61")
    # c2.save()
    customers = Customer.objects.count()
    return HttpResponse(f"Ok Done , we have {customers} customers")


def customers(request):
    data= Customer.objects.all() # ORM (Object relation master)Select* customers
    return render(request, 'customers.html',{customers:data})
