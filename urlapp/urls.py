from django.conf.urls import url

from .views import UrlView, UrlRequestView, UrlCreateView


urlpatterns = [
    url(r'^home/$', UrlView.as_view(), name='home'),
    url(r'^short/(?P<id>[0-9a-z-]+)$', UrlRequestView.as_view(), name='short'),
    url(r'^create/$', UrlCreateView.as_view(), name='create'),
]
