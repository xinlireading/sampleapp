from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    # /ckeditordemo/1/
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
]
