from django.conf.urls import patterns, include, url
from app import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^tweets/(?P<start>[0-9]+)/(?P<quantity>[0-9]+)$', views.tweets, name='tweet_api'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'.*', views.error),
)
