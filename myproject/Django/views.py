import json
from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CourseRegistration
# Create your views here.

@csrf_exempt
def register_student(request):
    try:
        if request.method=="POST":
            data = json.loads(request.body)
            CourseRegistration.objects.create(
                name=data["name"],
                email=data["email"],
                course=data["course"],
                phone=data["phone"]
            )
            return JsonResponse({"status":"success","message":"Registration Successful"},status=201)
        else:
            return JsonResponse({"error":"only Post method is allowed"},status=400)
    except Exception as e:
        print(e)
        return JsonResponse({"error":"something is went wrong"},status=500)


def get_registrations(request):
    if request.method=="GET":
        data =list(CourseRegistration.objects.values())
        return JsonResponse({"registrations":data},status=200)
    return JsonResponse({"message":"Invalid request"},status=405)