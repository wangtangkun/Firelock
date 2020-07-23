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
        baoliu=request.POST.get("baoliu")
        print("name",name,"password",password,"Keep_account",Keep_account)
    error_msg = ""
    if request.POST.get("name")=="123":error_msg = "用户名密码错误!"
    return render(request, "login/login.html", {"error_msg": error_msg})