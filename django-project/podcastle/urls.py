"""podcastle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from shows.views import *

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  # A Couple of Suggested URL Configs
                  # url(r'^podcastle/$', HomePageView.as_view()),
                  url(r'^(?P<slug>[\w-]+)/$', ShowDetailView.as_view(), name='shows'),
                  url(r'^.+/(?P<slug>[\w-]+)/$', EpisodeDetailView.as_view(), name='episodes'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'PodCastle Admin'
admin.site.site_title = 'PodCastle Admin'