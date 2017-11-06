from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.views import View
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from weibo.models import *
# Create your views here.


# @method_decorator(login_required, 'dispatch')
# class HomePageView(View):
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
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    # wbs = WeiBo.objects.all().order_by('-time_create')
    return render(request, 'weibo/homepage.html', {
        'wb_user': wb_user,
        # 'wbs': wbs
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
    wbs = WeiBo.objects.filter(user=wb_user).order_by('-time_create')
    return render(request, 'weibo/user_page.html', {
        'wb_user': wb_user,
        'wbs': wbs
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
