from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math
from django.views.decorators.csrf import csrf_exempt
import json
from basic.models import userProfile,Employee
from django.db.utils import IntegrityError
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


def pagination(request):
    data = ["apple","banana","carrot","grapes","watermelon","kiwi","pineapple","custard_apple","strawberry","blueberry","dragon_fruit"]
    page = int(request.GET.get("page",1))
    limit =int(request.GET.get("limit",3))
    start = (page-1)*limit
    end = page * limit
    total_pages = math.ceil(len(data)/limit)
    result = data[start : end]
    res = { "status":"success","current_page":page,"total_pages":total_pages,"data":result}
    return JsonResponse(res)

@csrf_exempt
def createData(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)#dictionary
            name=data.get("name")#taking name property from dictionary
            age = data.get("age")#taking age property from dictionary
            city =data.get("city")#taking city property from dictionary
            userProfile.objects.create(name=name,age=age,city=city)
            print(data)
        return JsonResponse({"status":"succes","data":data,"statuscode":201},status=201)
    except Exception as e:
        return JsonResponse({"statuscode":500,"message":"internal server error"})
    
@csrf_exempt
def createProduct(request):
    if request.method=="POST":
        data = json.loads(request.body)
        print(data)
    return JsonResponse({"status":"success","data":data,"statuscode":201})

@csrf_exempt
def createEmployee(request):
    try:
        if request.method=="POST":
            data = json.loads(request.body)
            Employee.objects.create(emp_name=data.get("name"),emp_salary=data.get("salary"),emp_email=data.get("email"))
        return JsonResponse({"status":"succes","data":data,"statuscode":201},status=201)
    except IntegrityError as e:
        return JsonResponse({"status":"error","message":"duplicates are not allowed"},status=401)
    finally:
        print("done")
    
