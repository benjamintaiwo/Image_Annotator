"""img_annotator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns


from annotator.views import (
    annotate,
	AnnotationsList,
	AnnotationsCreate,
	AnnotationsUpdate,
	AnnotationsRetrieve
	)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', annotate, name='annotate'),
    url(r'^api/annotate/$', AnnotationsList.as_view(), name='annotate-list'),
    url(r'^api/annotate/create/$', AnnotationsCreate.as_view(), name='annotate-create'),
    url(r'^api/annotate/(?P<pk>[\d]+)/$', AnnotationsRetrieve.as_view(), name='annotate-retrieve'),
    url(r'^api/annotate/(?P<pk>[\d]+)/edit/$', AnnotationsUpdate.as_view(), name='annotate-update'),

]

urlpatterns = format_suffix_patterns(urlpatterns)