
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/session/', include('commons.urls')),
    path('api/users/', include('customuser.urls')),
    path('api/file/', include('file.urls')),
    path('api/folder/', include('folder.urls')),
    path('api/bibliometric/', include('commons.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
