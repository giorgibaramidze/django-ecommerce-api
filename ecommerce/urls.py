from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from apps.category import views as category_view
from apps.product import views as product_view

router = DefaultRouter()
router.register(r"category", category_view.CategoryViewSet) 
router.register(r"brand", category_view.BrandViewSet)
router.register(r"product", product_view.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
