from django.conf.urls import patterns, url

from stackclient.views import RegisterView


urlpatterns = patterns('',
                       url(r'^register$', RegisterView.as_view(), name='register'),
)
