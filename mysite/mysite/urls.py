"""mysite URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from photohost.views import PhotoView, UserFormView, DetailView, PhotoCreate, PhotoDelete, PhotoUpdate


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^photohost/$', PhotoView.as_view(), name='photo_list'),
    url(r'^photohost/(?P<pk>[0-9]+)/$', DetailView.as_view(), name = 'detail'),
    url(r'^register/$', UserFormView.as_view(), name='register'),    
    url(r'photohost/add/$', PhotoCreate.as_view(), name = 'photo-add'),
    url(r'photohost/(?P<pk>[0-9]+)/delete/$', PhotoDelete.as_view(), name = 'photo-delete'),
    url(r'photohost/photo/(?P<pk>[0-9]+)/$', PhotoUpdate.as_view(), name = 'photo-update'),
    ] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
