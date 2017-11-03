from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from weibo.models import *
# Create your views here.


@login_required
def homepage(request):
    wb_user = get_object_or_404(WBUser, id=request.user.id)
    # wbs = WeiBo.objects.all().order_by('-time_create')
    return render(request, 'weibo/homepage.html', {
        'wb_user': wb_user,
        # 'wbs': wbs
    })


def user_page(request):
    uid = request.GET.get('uid')
    wb_user = get_object_or_404(WBUser, id=uid)
    wbs = WeiBo.objects.filter(user=wb_user).order_by('-time_create')
    return render(request, 'weibo/user_page.html', {
        'wb_user': wb_user,
        'wbs': wbs
    })

