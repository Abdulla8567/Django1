from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"aboutus.html")

def sample(request):
    print(request)
    qp1=request.GET.get("name")
    qp2=request.GET.get("city")
    return HttpResponse(f"{qp1} is from {qp2}")

def sample1(request):
     info =  {"data":[{"name":"Abdulla","city":"Hyderabad","gender":"Male","course":"python"},{"name":"Kiran","city":"Hyderabad","gender":"Male","course":"python"},{"name":"Baseer","city":"Hyderabad","gender":"Male","course":"python"}]}
     return JsonResponse(info)
    # return JsonResponse({"data":["fridze","tv","washingmachine"]})
    #   return JsonResponse([1,2,3,4],safe=False)