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

def product_info(request):
    product_name = request.GET.get("product","Washing Machine")
    quantity = int(request.GET.get("quantity",3))
    price = int(request.GET.get("price",75000))
    data = {"product":product_name,"quantity":quantity,"price":price,"total_price":quantity*price}
    return JsonResponse(data)

def filteringData(request):
    data = [1,2,3,4,5,6,7,8,9,10]
    filtered_data = []
    qp = request.GET.get("nums",2)
    for x in data:
        if x % qp == 0:
            filtered_data.append(x)
    # return JsonResponse(filtered_data,safe=False)
    return JsonResponse({"data":filtered_data})

def filter_city(request):
    student_data = [{"name":"durgaprasasd","city":"hyd"},{"name":"Abdulla","city":"hyd"},{"name":"SaiKiran","city":"bnglr"},{"name":"Basheer","city":"bnglr"}]
    qp3 = request.GET.get("city","hyd")
    student_details = []
    for x in student_data:
        if x["city"] == qp3:
            student_details.append(x)
    return JsonResponse({"Details":student_details})
