"""
URL configuration for watermark_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# project/urls.py (watermark_app)
# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls.static import static
# from django.views.generic import TemplateView  # Import TemplateView

# from watermark_app import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Add this line
#     path('embedding_extracting/', include('watermark.urls')),  # Include your app's urls
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# project/urls.py (watermark_app)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

from watermark_app import settings

from watermark.views import home  # Import the 'home' view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),  # Set the 'home' view for the root URL '/'
    # path('embedding_extracting/', include('watermark.urls')),  # Include your app's urls
    path('', include('watermark.urls')),  # Include your app's urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

