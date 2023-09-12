# Shopaholic-m93
Shoes Shopping website

# ShoesOnlineShop

ShoesOnlineShop is a web application built using Django that offers an online shopping experience for shoes. It provides various features for users to browse, shop, and manage their cart.

## Features

- User authentication and registration
- User roles (customer, admin, etc.)
- Browse products by category, brand, color, and size
- View detailed product information, including the latest price
- Add products to the cart and manage the cart
- Secure checkout process
- User profiles with personal information and addresses
- Scheduled tasks for sending emails and other notifications
- API endpoints for accessing product information
- Admin dashboard for managing products, orders, and users
- ...

## Setup

1. Clone the repository:

   
   git clone https://github.com/RaziyeNikookolah/ShoesOnlineShop.git

2. Create a virtual environment:

    cd ShoesOnlineShop
    python -m venv venv


3. Activate the virtual environment:

    On macOS and Linux: 

        source venv/bin/activate

    On Windows:

        venv\Scripts\activate

4. Install the dependencies:
    
    pip install -r requirements.txt

5. Set up the database:

    python manage.py migrate

6. Create a superuser (admin account) for accessing the admin dashboard:

    python manage.py createsuperuser


7. Run Docker to set up the containers for Celery, Redis, and Celery Beat:

docker-compose up -d

8. Run the development server:

    python manage.py runserver

9. Open your browser and go to http://localhost:8000 to access the application.


## Usage
    Register an account or log in if you already have one.
    Browse products by navigating through different categories, brands, colors, and sizes.
    View detailed information about a product on its individual page.
    Add products to your cart and proceed to checkout.
    Update your profile details and manage addresses.
    Administrators can log in to the admin dashboard at http://localhost:8000/admin to manage products, orders, and users.
Contributing
    Contributions to ShoesOnlineShop are welcome! If you have any bug fixes, enhancements, or new features to propose, please submit a pull request.

## License
    This project is licensed under the MIT License.

