from django.conf.urls import url
from weibo import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    # url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'^update', views.wb_update, name='update'),
    # url(r'^update', views.WBUpdate.as_view(), name='update'),
    # url(r'^u', views.UserPageView.as_view(), name='upage'),
    url(r'^comment', views.wb_comment, name='comment'),
    url(r'^forward', views.wb_forward, name='forward'),
    url(r'^follow', views.user_follow, name='follow'),
    url(r'^unfollow', views.user_unfollow, name='unfollow'),
    url(r'^u', views.user_page, name='upage'),
]
