from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from backend.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('smart_cart.urls')),

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

