# "address book" for the products app
# Import the necessary tools
from django.urls import path
from .views import ProductList

# This list defines the specific URL paths within the 'products' app
urlpatterns = [
    # When a request comes to the root URL of this app, it will be handled by 'ProductList' view
    # Give it a name for easy reference!
    path('', ProductList.as_view(), name='product-list'),
]