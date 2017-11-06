from django.conf.urls import url
from account.views import *

urlpatterns = [
    url(r'^register', RegisterView.as_view(), name='register'),
    url(r'^login', LogInView.as_view(), name='login'),
    url(r'^logout', LogOutView.as_view(), name='logout'),
]
