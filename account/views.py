from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from weibo.models import WBUser
# Create your views here.


def register(request):
    """
    用户注册
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        # 注意，此处检验用户名必须用 User，User 包含了普通用户 UBUser 与超级用户 superuser
        is_exist = User.objects.filter(username=username)
        if password == password2 and not is_exist:
            # 此处创建普通用户，使用 WBUser
            user = WBUser.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            login(request, user)
            # 使用命名空间跳转页面
            return redirect('wb:homepage')
        else:
            return HttpResponse('密码不一致或用户名已存在')
    else:
        # 跳转至主页
        return redirect('/')


def log_in(request):
    """
    用户登录
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('wb:homepage')
        else:
            return HttpResponse('密码错误或用户名不存在')
    else:
        return redirect('/')


def log_out(request):
    """
    用户登出
    """
    logout(request)
    return redirect('/')
