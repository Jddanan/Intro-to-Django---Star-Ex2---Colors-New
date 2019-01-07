from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^colors/', include('colors.urls')),
    url(r'^admin/', admin.site.urls),
]