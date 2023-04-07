from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from core.views import contact, index

urlpatterns = [
    
    path('', include('core.urls')),
    path('deshboard/', include('deshboard.urls')),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
] 


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 