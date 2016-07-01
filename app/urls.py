from django.conf.urls import url, patterns
import views

urlpatterns = patterns('',
    url(r'^$', 'main.views.main_page'),
    url(r'^photo/$', views.PhotoList.as_view(), name='myphoto-list'),
    url(r'^photo/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view(), name='myphoto-detail'),
)
