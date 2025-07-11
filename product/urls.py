from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import ProductViews

router =  DefaultRouter()
router.register(r'product', ProductViews, basename='ProductViews')

urlpatterns = [
    path('', include(router.urls))
]

