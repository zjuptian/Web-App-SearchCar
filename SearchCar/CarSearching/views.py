from django.shortcuts import render
from CarSearching.get_car_price import searchcar
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
  return render(request, 'CarSearching/layout.html')

def car_list(request):
    brand=request.GET['brand']
    result = searchcar(brand)
    context = {'cars':result}
    print(context)
    return render(request, 'CarSearching/car_list.html',context)

def framec(request):
    return render(request, 'CarSearching/framec.html')
