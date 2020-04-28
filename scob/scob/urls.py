"""scob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import main_page, login_page, register_page, logout_page, contact_page, about_page
from .views import search_page,cart_page

from django.conf import settings
from django.conf.urls.static import static
from courses.views import CoursesDetailView,courses_list_view
from products.views import ProductDetailView,product_list_view
from masters.views import MasterDetailView,master_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('login', login_page),
    path('register', register_page),
    path('logout', logout_page),
    path('contact-us', contact_page),
    path('about-us', about_page),
    path('search', search_page),
    path('courses', courses_list_view),
    path('products', product_list_view),
    path('masters', master_list_view),
    path('cart', cart_page),
    path('courses/<pk>', CoursesDetailView.as_view()),
    path('products/<pk>', ProductDetailView.as_view()),
    path('masters/<pk>', MasterDetailView.as_view()),
]

if settings.DEBUG:  # add static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
