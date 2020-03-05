from django.shortcuts import render,HttpResponse,redirect,reverse
from django.http.response import  JsonResponse
# Create your views here.


def login(request):
    '''
    用户登录
    :param request:
    :return:
    '''
    if request.method=="POST":
        name=request.POST.get("name")
        password=request.POST.get("password")
        print("name",name,"password",password)
    error_msg = ""
    return render(request, "login.html", {"error_msg": error_msg})