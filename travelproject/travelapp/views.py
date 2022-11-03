from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


# Create your views here.
# def addition(request):
#     return render(request,.html,)
def home(request):
    # state="karnataka"
    obj=place.objects.all()
    obj2=team.objects.all()
    return render(request,'index.html',{'result':obj,'answer':obj2})
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     ans = x + y
#     sub = x-y
#     multi =x*y
#     div=x/y
#     return render(request,'result.html',{'result':ans,'answer':sub,'value':multi,'ans':div})

# def about(request):
#     return render(request,'about.html')
# def info(request):
#     return HttpResponse("developed by ashin")
