from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseRedirect
from urlapp.views import UrlView


urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('home/')),
    url('^', include('urlapp.urls', namespace='urlapp')),
    url(r'^home/', UrlView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
]
