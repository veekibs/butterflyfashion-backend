# Contains the "brain" - the logic that handles requests for the product data
# Import the necessary tools from Django Rest Framework + local files
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# This view is for listing all the products in the database
# Uses a built-in "generic" view from DRF, which makes it very simple + powerful
class ProductList(generics.ListAPIView):
    # 'queryset' tells this view which data to fetch from the database (in this case, all products)
    queryset = Product.objects.all()
    # 'serializer_class' tells the view to use ProductSerializer to format the data
    serializer_class = ProductSerializer