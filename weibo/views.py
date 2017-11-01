from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def homepage(request):
    user = request.user
    return HttpResponse(str(user))
