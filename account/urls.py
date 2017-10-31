from django.conf.urls import url
from account.views import *

urlpatterns = [
    url(r'^register', register, name='register'),
    url(r'^login', log_in, name='login'),
    url(r'^logout', log_out, name='logout'),
]
