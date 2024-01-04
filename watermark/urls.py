# # watermark/urls.py
# from django.urls import path

# from watermark_app import settings
# from .views import home, embed

# app_name = 'watermark'  # Add the app name (namespace)

# urlpatterns = [
#     path('', home, name='home'),
#     path('embed/', embed, name='embed'),
#     # Additional paths as needed
# ]




# **********************************main
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('embed_extract/', views.embed_extract, name='embed_extract'),
# ]



# watermark/urls.py
from django.urls import path
from .views import home, index, index1, color1, embed_extract_view, embed_extract_level2_view, embed_extract_color_view

urlpatterns = [
    path('', home, name='home'),  # Use the 'home' view for the root URL
    path('index/', index, name='index'),  # Use the 'index' view for /index/
    path('index1/', index1, name='index1'),  # Use the 'index' view for /index/
    path('color1/', color1, name='color1'),  # Use the 'index' view for /index/
    path('embed_extract/', embed_extract_view, name='embed_extract'),
    path('embed_extract_level2/', embed_extract_level2_view, name='embed_extract_level2'),
    path('embed_extract_color/', embed_extract_color_view, name='embed_extract_color'),
    # other URL patterns
]




# urls.py(watermark)
# from django.urls import path
# from .views import index, embed_extract_view
# from django.views.generic import TemplateView

# urlpatterns = [
#     path('', TemplateView.as_view(template_name='watermark/home.html'), name='home'),
#     path('index.html', TemplateView.as_view(template_name='watermark/index.html'), name='index'),
    # path('', index, name='index'),
    # path('embed_extract/', embed_extract_view, name='embed_extract'),
    # other URL patterns
# ]


# ***************************************





# # watermark/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('embed_extract/', views.embed_extract_view, name='embed_extract'),
# ]


# watermark/urls.py

# from django.urls import path
# from . import views

# # app_name = 'watermark'

# urlpatterns = [
#     path('', views.index, name='index'),
#     # Other URL patterns for the 'watermark' app...
# ]

