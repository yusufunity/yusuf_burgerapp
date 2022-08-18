from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import *


urlpatterns=[

	path('menu/', MenuPage.as_view(), name='menu'),

	path('about/',AboutPage.as_view(),name='about'),
	path('book/',BookPage.as_view(),name='book'),
	path('',  HomePage.as_view(), name='index'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
