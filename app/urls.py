from django.conf.urls import url, include
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # url(r'^$', 'main.views.main_page'),
    url(r'^photo/$', views.PhotoList.as_view(), name='myphoto-list'),
    url(r'^photo/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view(), name='myphoto-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
