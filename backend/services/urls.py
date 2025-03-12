from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceCategoryViewSet, SalonServiceViewSet,
    MassageServiceViewSet, LaundryServiceViewSet, LaundryItemViewSet
)

router = DefaultRouter()
router.register(r'categories', ServiceCategoryViewSet)
router.register(r'salon', SalonServiceViewSet)
router.register(r'massage', MassageServiceViewSet)
router.register(r'laundry', LaundryServiceViewSet)
router.register(r'laundry-items', LaundryItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]