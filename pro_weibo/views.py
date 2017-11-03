from django.shortcuts import render
from django.views import View
from weibo.models import WBUser

# Create your views here.


class Index(View):
    def get(self, request):
        users = WBUser.objects.all().order_by('-id')[:10]
        return render(request, 'index.html', {
            'users': users
        })

#
# def index(request):
#     users = WBUser.objects.all().order_by('-id')[:10]
#     return render(request, 'index.html', {
#         'users': users
#     })
