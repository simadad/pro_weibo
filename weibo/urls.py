from django.conf.urls import url
from weibo import views

urlpatterns = [
    # url(r'^$', views.homepage, name='homepage'),
    url(r'^$', views.HomePageView.as_view(), name='homepage'),
    # url(r'^u', views.user_page, name='upage'),
    url(r'^u', views.UserPageView.as_view(), name='upage'),
]
