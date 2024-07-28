from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripViewSet, ExpenseViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'trips', TripViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
