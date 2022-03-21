from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view
from rest_framework.authtoken import views


admin.site.site_header = 'TPL Backend'
admin.site.index_title = 'TPL Backend'
admin.site.site_title = 'TPL Backend'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', views.obtain_auth_token),
    path('api/auth/', include('user.urls')),
    path('api/articles/', include('article.urls')),
    path('api/routes/', include('route.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns.append(
        path('openapi/', get_schema_view(
            title="School Service",
            description="API documentation"
        ), name='openapi-schema'),
    )
