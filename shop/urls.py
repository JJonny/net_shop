from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<category_id>\d+)/$', views.tea_category, name='tea'),
    url(r'^(?P<slug>[\w-]+)/$', views.tea_description, name='tea-description'),
]
