from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import landing_page

urlpatterns = [
    path('', landing_page, name='home'),
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('', include('users.urls')),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)