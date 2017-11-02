from django.shortcuts import render
from weibo.models import WBUser

# Create your views here.


def index(request):
    users = WBUser.objects.all().order_by('-id')[:10]
    return render(request, 'index.html', {
        'users': users
    })
