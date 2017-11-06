from django.conf.urls import url
from weibo import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    # url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'^update', views.wb_update, name='update'),
    # url(r'^update', views.WBUpdate.as_view(), name='update'),
    url(r'^u', views.user_page, name='upage'),
    # url(r'^u', views.UserPageView.as_view(), name='upage'),
    url(r'^comment', views.wb_comment, name='comment'),
]
