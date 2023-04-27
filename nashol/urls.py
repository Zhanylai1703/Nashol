from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.bitches import views

from apps.users.views import (
    UserViewSet,
    RegisterView,
    LoginView,
    LogoutView,
    )


schema_view = get_schema_view(
   openapi.Info(
      title="EPAM",
      default_version='v1',
      description="username:user / password:user",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'bitch/', views.BitchViewSet, basename='bitches'),
router.register(r'categories', views.CategoryViewSet)
router.register(r'image/', views.BitchViewSet,basename="images")
router.register(r'user/', UserViewSet,basename="users")

api_v1 = [
    path('reg/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include(api_v1)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'
        ),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), 
        name='schema-redoc'
        ),
]
