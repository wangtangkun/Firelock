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
        Keep_account=request.POST.get("Keep_account")
        email=request.POST.get("email")
        print(email)
        print("name",name,"password",password,"Keep_account",Keep_account,email)
    error_msg = ""
    if request.POST.get("name")=="123":error_msg = "用户名密码错误!"
    #2123
    return render(request, "login/login.html", {"error_msg": error_msg})

