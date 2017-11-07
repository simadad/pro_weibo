from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# from django.views import View
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from weibo.models import *
# Create your views here.


# @method_decorator(login_required, 'dispatch')
# class HomePageView(View):
#    """
#   class base views
#   """
#     def get(self, request):
#         wb_user = get_object_or_404(WBUser, id=request.user.id)
#         # wbs = WeiBo.objects.all().order_by('-time_create')
#         return render(request, 'weibo/homepage.html', {
#             'wb_user': wb_user,
#             # 'wbs': wbs
#         })


@login_required
def homepage(request):
    """
    个人中心
    """
    user = get_object_or_404(WBUser, id=request.user.id)
    wbs = WeiBo.objects.filter(user__in=user.followers.all()).order_by('-time_create')[:10]
    return render(request, 'weibo/homepage.html', {
        'user': user,
        'wbs': wbs
    })


# class UserPageView(View):
#     def get(self, request):
#         uid = request.GET.get('uid')
#         wb_user = get_object_or_404(WBUser, id=uid)
#         wbs = WeiBo.objects.filter(user=wb_user).order_by('-time_create')
#         return render(request, 'weibo/user_page.html', {
#             'wb_user': wb_user,
#             'wbs': wbs
#         })


def user_page(request):
    """
    用户主页
    """
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user = get_object_or_404(WBUser, id=request.user.id)
    wbs = WeiBo.objects.filter(user=wb_user).order_by('-time_create')
    return render(request, 'weibo/user_page.html', {
        'wb_user': wb_user,
        'wbs': wbs,
        'user': user
    })


# class WBUpdate(View):
#     def post(self, request):
#         wb_user = get_object_or_404(WBUser, id=request.user.id)
#         msg = request.POST.get('msg')
#         wb = wb_user.update(msg)
#         return HttpResponse(render(request, 'weibo/new_wb.html', {'wb': wb}))


def wb_update(request):
    """
    发送微博
    """
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    msg = request.POST.get('msg')
    wb = wb_user.update(msg)
    return HttpResponse(render(request, 'weibo/new_wb.html', {'wb': wb}))


def wb_comment(request):
    """
    微博评论
    """
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    msg = request.POST.get('msg')
    wid = request.POST.get('wid')
    wb = get_object_or_404(WeiBo, id=wid)
    comment = wb.comment_this(user=wb_user, text=msg)
    return HttpResponse(render(request, 'weibo/new_comm.html', {'comm': comment}))


def wb_forward(request):
    """
    微博转发
    """
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    msg = request.POST.get('msg')
    wid = request.POST.get('wid')
    wb = get_object_or_404(WeiBo, id=wid)
    new_wb = wb_user.forward(wb)
    if msg:
        new_wb.comment_this(user=wb_user, text=msg)
    # redirect 接受 url name 参数，返回一个可以被 views return 返回的对象 HttpResponseRedirect
    response = redirect('wb:upage')
    # HttpResponseRedirect['Location'] 为跳转地址，下面的代码为地址直接拼接 get 参数
    response['Location'] += '?uid={uid}'.format(uid=wb_user.id)
    # HttpResponseRedirect 对象可以直接 return 返回，页面跳转到 response['Location'] 所指定的地址
    return response


def user_follow(request):
    """
    关注用户
    """
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user = get_object_or_404(WBUser, id=request.user.id)
    user.follow(wb_user)
    return HttpResponse()


def user_unfollow(request):
    """
    解除关注
    """
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    user = get_object_or_404(WBUser, id=request.user.id)
    user.unfollow(wb_user)
    return HttpResponse()
