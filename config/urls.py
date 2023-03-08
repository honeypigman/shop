from django.contrib import admin
from django.urls import path
from django.urls import include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Shop",
        default_version='0.0.1',
        description="""
        Django Simple Shop
        - 회원관리
        - 주문관리
        - 배송관리
        - 현황관리
        """,
        terms_of_service="",
        contact=openapi.Contact(email="honeypigman@gmail.com"),
        license=openapi.License(name="honeypigman@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
]
