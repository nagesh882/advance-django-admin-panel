from django.urls import path, include
from rest_api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
router = DefaultRouter()

router.register("register", views.userViewSet, basename="register")

router.register("product", views.productViewSet, basename="product")

urlpatterns = [
 
    path("", include(router.urls)),
    path('getToken/', include('rest_framework.urls', namespace='rest_framework')),

]