from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"Category", views.CategoryViewSet)
router.register(r"Product", views.ProductViewSet)
router.register(r"Customer", views.CustomerViewSet)
router.register(r"Operator", views.OperatorViewSet)
router.register(r"Order", views.OrderViewSet)
router.register(r"OrderItem", views.OrderItemViewSet)
router.register(r"Bill", views.BillViewSet)

urlpatterns = [path("", include(router.urls))]
