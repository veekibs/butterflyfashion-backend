"""
URL configuration for butterfly_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# Main address book for entire project
# Import the necessary tools
from django.contrib import admin
from django.urls import path, include

# This is the main URL routing configuration for the entire project
urlpatterns = [
    # The standard URL for the Django admin panel
    path('admin/', admin.site.urls),
    # This line tells Django that any URL starting with 'api/products/'
    # should be handled by the URL patterns we defined in the products/urls.py file
    path('api/products/', include('products.urls')),
]
