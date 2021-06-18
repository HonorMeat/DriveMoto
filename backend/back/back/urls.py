from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from shop.views import ProductViews

router = routers.DefaultRouter()
router.register(r'product', ProductViews, 'product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
