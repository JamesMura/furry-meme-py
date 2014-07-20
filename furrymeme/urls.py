from django.conf.urls import patterns, include, url

from stackclient.views import HomeView


urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home'),
                       url(r'^c/', include('stackclient.urls')),
)
