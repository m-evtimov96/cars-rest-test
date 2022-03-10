from django.urls import path, include
from .views import CarBrandView, CarModelView, UserCarView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('car-brands', CarBrandView)
router.register('car-models', CarModelView)
router.register('user-cars', UserCarView)

urlpatterns = [
    path('', include(router.urls)),
]