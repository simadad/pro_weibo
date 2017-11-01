from django.conf.urls import url
from weibo import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^u', views.user_page, name='upage'),
]
