from django.contrib.auth.models import User
from listings.models import Listing

# Find all objects
listings = Listing.objects.all()

# Get a single object
listing = Listing.objects.get(title="Django Beginner")

# Filter objects
filtered_listings = Listing.objects.filter(price__lt=50000)

# Exclude objects
excluded_listings = Listing.objects.exclude(city="New York")

# Filter using category
category_listings = Listing.objects.filter(category__name="School")

# Order objects
ordered_listings = Listing.objects.order_by("-price")

# Chain queries
chained_listings = (
    Listing.objects.filter(bedrooms__gte=3)
    .exclude(city="Los Angeles")
    .order_by("price")
)

# Order objects
user_ano = User.objects.get(username__startswith="ano")
user_ano = User.objects.get(username__iexact="ano")
