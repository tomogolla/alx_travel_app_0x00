from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with dummy data'

    def handle(self, *args, **kwargs):
        # Create users
        users = [User.objects.create_user(username=fake.user_name(), password='pass1234') for _ in range(5)]

        # Create listings
        listings = []
        for _ in range(5):
            listing = Listing.objects.create(
                title=fake.sentence(),
                description=fake.text(),
                location=fake.city(),
                price_per_night=random.randint(50, 300),
                owner=random.choice(users)
            )
            listings.append(listing)

        # Create bookings
        for _ in range(10):
            listing = random.choice(listings)
            start_date = fake.date_this_month()
            end_date = start_date + timedelta(days=random.randint(1, 5))
            Booking.objects.create(
                listing=listing,
                user=random.choice(users),
                start_date=start_date,
                end_date=end_date,
                total_price=random.randint(100, 1000)
            )

        # Create reviews
        for _ in range(10):
            Review.objects.create(
                listing=random.choice(listings),
                user=random.choice(users),
                rating=random.randint(1, 5),
                comment=fake.sentence()
            )

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully!"))
