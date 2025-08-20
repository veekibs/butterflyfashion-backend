# Blueprint for product data in the database
# Import the necessary tools from Django
from django.db import models

# Define Product model
# Each class variable represents a field in the database table
class Product(models.Model):
    # Simple text field for the product's name, with a maximum length of 255 characters
    name = models.CharField(max_length=255)
    # A larger text field for the product description
    # It's optional (can be blank/null)
    description = models.TextField(blank=True, null=True)
    # A field for the price, using a DecimalField for accurate financial calculations
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # A field to store the URL or path to the product's image
    image_url = models.CharField(max_length=1024)
    # A field to categorise the product, with predefined choices for "preteen" or "teen"
    category = models.CharField(max_length=50, choices=[('preteen', 'Preteen'), ('teen', 'Teen')])

    is_new_arrival = models.BooleanField(default=False)
    class SubCategory(models.TextChoices):
        TOP = 'top', 'Top'
        BOTTOM = 'bottom', 'Bottom'
    
    sub_category = models.CharField(
        max_length=50,
        choices=SubCategory.choices,
        default=SubCategory.TOP, 
    )
    
    # Helper function that tells Django what to display when a Product object is printed
    # In this case, it will just show the product's name!
    def __str__(self):
        return self.name