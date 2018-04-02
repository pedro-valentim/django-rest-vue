from django.conf import settings
from django.conf.urls import url, include, static
# from django.contrib import admin
from rest_framework import routers
from backend import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
