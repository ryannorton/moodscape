from django.conf.urls import patterns, include, url
from app import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'.*', views.error),
)
