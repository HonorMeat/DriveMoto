from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
# from shop.views import ProductViews

# router = routers.DefaultRouter()
# router.register(r'product', ProductViews, 'product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
