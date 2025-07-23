

```markdown
# ALX Travel App - 0x00: Database Modeling & Data Seeding

This module is part of the `alx_travel_app_0x00` project and focuses on defining the core database models, implementing serializers for API representation, and creating a data seeding script using Django's management commands.

---

## Project Structure

```

alx\_travel\_app\_0x00/
├── listings/
│   ├── models.py          # Defines Listing, Booking, and Review models
│   ├── serializers.py     # Serializers for the above models
│   └── management/
│       └── commands/
│           └── seed\_data.py  # Command to seed the database

````

---

## Models

Defined in `listings/models.py`:

### Listing
- `id` (UUID): Primary Key
- `title`: CharField
- `description`: TextField
- `location`: CharField
- `price_per_night`: Decimal
- `owner`: ForeignKey to `User`
- `created_at`: DateTime

### Booking
- `id` (UUID): Primary Key
- `listing`: FK to `Listing`
- `user`: FK to `User`
- `start_date`, `end_date`: DateField
- `total_price`: Decimal
- `created_at`: DateTime

### Review
- `id` (UUID): Primary Key
- `listing`: FK to `Listing`
- `user`: FK to `User`
- `rating`: IntegerField
- `comment`: TextField
- `created_at`: DateTime

---

## Serializers

Located in `listings/serializers.py`. These convert model instances into JSON and validate incoming data.

- `ListingSerializer`
- `BookingSerializer`
- `ReviewSerializer`

---

## Database Seeding

A custom management command (`seed_data`) generates sample users, listings, bookings, and reviews using the **Faker** library.

### Usage

```bash
# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Seed the database with fake data
python manage.py seed_data
````

### Output

* 5 Users
* 5 Listings
* 10 Bookings
* 10 Reviews

---

## Requirements

Make sure to install the required dependencies:

```bash
pip install Faker
```

---

## Objective

* Lay the groundwork for the travel app with realistic, relational data.
* Enable testing of APIs with sample data.
* Ensure modularity and scalability for later stages of the project.

---

## Notes

* All UUIDs are auto-generated.
* `User` model is Django’s default.
* The `seed_data` script uses random selections to create a varied dataset.

---

## Contact

Developed by **Thomas Ogolla**
For inquiries or feedback: [LinkedIn](https://www.linkedin.com/in/tomogolla)

```
