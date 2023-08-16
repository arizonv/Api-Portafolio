from django.contrib import admin
from django.urls import path,include
from django.urls import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


