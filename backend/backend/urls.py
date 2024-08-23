# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Define a simple view for the root URL that returns a welcome message
def home_view(request):
    return HttpResponse("Welcome to the home page!")

urlpatterns = [
    # Admin panel URL for Django's built-in admin interface
    path('admin/', admin.site.urls),

    # Include URLs from the 'api' app, which handles API routes
    path('api/', include("api.urls")),

    # Include URLs for CKEditor file uploads
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Include URLs for CKEditor 5
    path("ckeditor5/", include('django_ckeditor_5.urls')),

    # Root URL pattern serving a simple welcome page
    path('', home_view),
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files (e.g., user-uploaded content) during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
