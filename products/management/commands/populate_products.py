# products/management/commands/populate_products.py

# This script will automatically populate the database with product information

from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    # Help message that will show up if you type --help
    help = 'Populates the database with the complete and final list of products'

    # Main function that will run when executing the script
    def handle(self, *args, **kwargs):
        # First, print a message to the console to show the script is running
        self.stdout.write('Deleting all existing products to ensure a clean slate...')
        # Delete all existing products to avoid creating duplicates if running the script again
        Product.objects.all().delete()
        self.stdout.write('Existing products deleted.')

        # This is the complete, combined list of all products from ALL JavaScript files
        products_data = [
            # From script.js / index.html
            {"name": "floral & slogan graphic drawstring thermal lined hoodie", "price": 12, "image_url": "clothes/blue hoodie.jpg", "category": "preteen"},
            {"name": "buffalo plaid zip up dual pocket hooded teddy jacket", "price": 20, "image_url": "clothes/teddy front.jpg", "category": "preteen"},
            {"name": "letter & floral print jeans", "price": 19, "image_url": "clothes/flower jeans.jpg", "category": "preteen"},
            {"name": "letter print striped trim drop shoulder sweatshirt dress", "price": 15, "image_url": "clothes/brown.jpg", "category": "preteen"},
            {"name": "panda & heart embroidery drop shoulder teddy jacket", "price": 21, "image_url": "clothes/panda jacket.jpg", "category": "preteen"},
            {"name": "japanese letter & figure graphic hoodie dress", "price": 15, "image_url": "clothes/anime.jpg", "category": "preteen"},
            {"name": "letter graphic kangaroo pocket drawstring thermal hoodie", "price": 14, "image_url": "clothes/cool.jpg", "category": "preteen"},
            {"name": "brown plaid print mini skirt", "price": 5, "image_url": "clothes/skirt.jpg", "category": "preteen"},
            {"name": "letter patched striped trim cricket sweater vest", "price": 11, "image_url": "clothes/vest.jpg", "category": "teen"},
            {"name": "letter graphic contrast collar thermal lined sweatshirt", "price": 17, "image_url": "clothes/blokecore.jpg", "category": "teen"},
            {"name": "shawl collar contrast teddy PU leather coat", "price": 40, "image_url": "clothes/shawl.jpg", "category": "teen"},
            {"name": "bear pattern teddy trousers", "price": 18, "image_url": "clothes/lol.jpg", "category": "teen"},
            {"name": "drop shoulder 3D ear teddy hoodie", "price": 11, "image_url": "clothes/teddy.jpg", "category": "teen"},
            {"name": "fuzzy trim open front coat", "price": 35, "image_url": "clothes/fuzzy.jpg", "category": "teen"},
            {"name": "floral print straight leg jeans", "price": 15, "image_url": "clothes/floral.jpg", "category": "teen"},
            {"name": "checkered & heart pattern sweater vest without tee", "price": 10, "image_url": "clothes/vestie.jpg", "category": "teen"},
            
            # From newarrivals.js
            {"name": "butterfly print cami top & zip up hoodie & sweatpants", "price": 26, "image_url": "clothes/cami set.jpg", "category": "preteen"},
            {"name": "sun & moon print high waist jeans", "price": 24, "image_url": "clothes/jeans.jpg", "category": "preteen"},
            {"name": "high neck solid tee", "price": 5, "image_url": "clothes/turtleneck.jpg", "category": "preteen"},
            {"name": "puff sleeve zip up dress", "price": 12, "image_url": "clothes/puff.jpg", "category": "preteen"},
            {"name": "striped & floral patched lettuce trim tee", "price": 7, "image_url": "clothes/flopo.jpg", "category": "preteen"},
            {"name": "mock neck letter embroidery top & trousers", "price": 25, "image_url": "clothes/brownie.jpg", "category": "preteen"},
            {"name": "camo print drop shoulder pullover & leggings", "price": 14, "image_url": "clothes/army.jpg", "category": "preteen"},
            {"name": "v neck ribbed knit dress with belt", "price": 11, "image_url": "clothes/dress.jpg", "category": "preteen"},
            {"name": "star print contrast tape side sweatpants", "price": 16, "image_url": "clothes/star sweatpants.jpg", "category": "teen"},
            {"name": "high waist tie front flap pocket cargo jeans", "price": 25, "image_url": "clothes/cjeans.jpg", "category": "teen"},
            {"name": "letter patched striped trim bomber jacket & sweatpants", "price": 27, "image_url": "clothes/bomber jacket.jpg", "category": "teen"},
            {"name": "ripped cut out straight leg jeans", "price": 24, "image_url": "clothes/rjeans.jpg", "category": "teen"},
            {"name": "solid ribbed knit crop knit top & knit leggings & duster cardigan", "price": 30, "image_url": "clothes/justbrown.jpg", "category": "teen"},
            {"name": "figure graphic drop shoulder zip up drawstring hoodie", "price": 17, "image_url": "clothes/hoodie.jpg", "category": "teen"},
            {"name": "letter graphic contrast collar crop tee", "price": 15, "image_url": "clothes/croptee.jpg", "category": "teen"},
            {"name": "letter graphic drop shoulder tee", "price": 11, "image_url": "clothes/tee.jpg", "category": "teen"},

            # From preteens.js
            {"name": "buckle strap flap pocket cargo pants", "price": 13, "image_url": "clothes/cargo.jpg", "category": "preteen"},
            {"name": "butterfly print sweatpants", "price": 9, "image_url": "clothes/sweat.jpg", "category": "preteen"},
            {"name": "knot front cargo trousers", "price": 13, "image_url": "clothes/poople.jpg", "category": "preteen"},
            {"name": "camo print straight leg jeans", "price": 21, "image_url": "clothes/camosplit.jpg", "category": "preteen"},
            {"name": "2pcs contrast tape pleated skirt", "price": 20, "image_url": "clothes/yuigoh.jpg", "category": "preteen"},
            {"name": "heart print jeans", "price": 21, "image_url": "clothes/heartprintj.jpg", "category": "preteen"},
            {"name": "allover heart print flare leg pants", "price": 8, "image_url": "clothes/heartflare.jpg", "category": "preteen"},
            {"name": "plaid & letter graphic drop shoulder shirt", "price": 16, "image_url": "clothes/greenplaid.jpg", "category": "preteen"},
            {"name": "colourblock raglan tee", "price": 11, "image_url": "clothes/bp.jpg", "category": "preteen"},
            {"name": "turtleneck lantern sleeve sweater", "price": 14, "image_url": "clothes/sweater.jpg", "category": "preteen"},
            {"name": "skull & floral print drop shoulder drawstring thermal costume hoodie", "price": 13, "image_url": "clothes/shood.jpg", "category": "preteen"},
            {"name": "ditsy floral print frill trim cami top", "price": 11, "image_url": "clothes/ditsy.jpg", "category": "preteen"},
            {"name": "2 in 1 graphic printed tee", "price": 7, "image_url": "clothes/animegal.jpg", "category": "preteen"},
            {"name": "floral & letter graphic drop shoulder zip up hoodie", "price": 12, "image_url": "clothes/ghood.jpg", "category": "preteen"},
            {"name": "mock neck crisscross hem tee", "price": 7, "image_url": "clothes/smile.jpg", "category": "preteen"},
            
            # From teens.js
            {"name": "high waist split thigh skirt", "price": 9, "image_url": "clothes/skirtt.jpg", "category": "teen"},
            {"name": "zip back pleated skirt", "price": 11, "image_url": "clothes/pskirt.jpg", "category": "teen"},
            {"name": "elastic waist wide leg trousers", "price": 12, "image_url": "clothes/wideleg.jpg", "category": "teen"},
            {"name": "flap pocket side chain detail buckled belted cargo trousers", "price": 17, "image_url": "clothes/gothtro.jpg", "category": "teen"},
            {"name": "eyelet embroidery ruffle trim tie backless top", "price": 7, "image_url": "clothes/whiteeye.jpg", "category": "teen"},
            {"name": "grunge off shoulder ruched crop tee", "price": 8, "image_url": "clothes/grunge.jpg", "category": "teen"},
            {"name": "3pcs solid backless halter top", "price": 15, "image_url": "clothes/halter.jpg", "category": "teen"},
            {"name": "scoop neck bell sleeve crop tee", "price": 8, "image_url": "clothes/black.jpg", "category": "teen"},
        ]

        # Remove any duplicate products to ensure database is clean 
        # Use the 'name' of the product as the unique identifier
        unique_products = {product['name']: product for product in products_data}.values()

        self.stdout.write('Populating the database with new products...')
        
        # Loop through each unique product in the list
        for product_data in unique_products:
            # For each product, create a new Product object in the database
            # The **product_data unpacks the dictionary to match the model fields (name=, price=, etc.)
            Product.objects.create(**product_data)
        
        # Print a success message to the console with the final count of products added
        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with {len(unique_products)} unique products!'))