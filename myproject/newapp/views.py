from django.shortcuts import render
from django.http import JsonResponse
from newapp.models import OrderDetails
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def  orderPlacing(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            order=OrderDetails.objects.create(
                orderid=data["order_id"],
                useremail=data["email"],
                amount=data["amount"],
                status=data["status"],
                mode=data["mode"]
                )
            print(order.transaction_id)
            x=order.transaction_id
            return JsonResponse({"status":"success",
                                 "message":"payment details updated successfully",
                                 "transaction_id":x},
                                 status=201)
        else:
            return JsonResponse({"error":"only post method is allowed"},status=400)
    except Exception as e:
        print(e)
        return JsonResponse({"error":"something went wrong"},status=500)