from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from rest_framework.schemas import get_schema_view
from rest_framework.authtoken import views

from article.templates_views import IndexTemplateView, LoginTemplateView


admin.site.site_header = 'TPL Backend'
admin.site.index_title = 'TPL Backend'
admin.site.site_title = 'TPL Backend'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name="home-page"),
    path('login/', auth_views.LoginView.as_view(template_name='register.html'), name='login-page'),
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
