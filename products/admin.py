# Tells Django admin panel to manage Product model
# # Import the necessary tools from Django + models file
from django.contrib import admin
from .models import Product

# Registers Product model with the Django admin site
# Allows for easy adding, editing + deletion products through the admin interface
admin.site.register(Product)