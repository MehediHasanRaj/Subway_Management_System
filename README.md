# Subway Management System

## Overview
The Subway Management System is a robust restaurant management software built using Django. It features user authentication, a REST API, and a user-friendly interface for customers and administrators. Customers can browse the menu and place orders, while administrators have full control over food items and user accounts, including CRUD operations.

## Features

### Customer Features:
- **Menu Browsing**: Customers can view food items, descriptions, and prices in an intuitive menu display.
- **Order Placement**: Users can place orders directly from the menu.

### Administrator Features:
- **Food Management**: Administrators can add, update, or delete menu items.
- **User Management**: Admins can manage user accounts.
- **Secure Authentication**: Access to administrative tools is protected by a secure user authentication system.

### Technical Features:
- **Django ORM**: Used for seamless interaction with the database.
- **REST API**: Designed for efficient communication between the frontend and backend.
- **Testing**: Comprehensive unit and integration tests to ensure software reliability.

## Tech Stack
- **Backend**: Django, Django REST Framework (DRF), Python
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MYSQL
- **Version Control**: Git

## Installation

### Prerequisites:
- Python 3.x
- pip (Python package manager)
- Git

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/MehediHasanRaj/Subway_Management_System
   cd subway-management-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application:
   - Customer Portal: `http://127.0.0.1:8000/`
   - Admin Portal: `http://127.0.0.1:8000/admin`

## Project Structure
```
subway-management-system/
├── subway/                 # Main Django project folder
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URLs
│   └── ...
├── menu/                   # App for managing menu items
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── urls.py             # App-specific URLs
│   └── ...
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript, and images
├── db.sqlite3              # SQLite database (default)
├── manage.py               # Django management script
└── requirements.txt        # Project dependencies
```

## API Endpoints
### Authentication:
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration

### Menu:
- `GET /api/menu/` - View all menu items
- `POST /api/menu/` - Add a new menu item (Admin only)
- `PUT /api/menu/<id>/` - Update a menu item (Admin only)
- `DELETE /api/menu/<id>/` - Delete a menu item (Admin only)

### Orders:
- `POST /api/orders/` - Place an order
- `GET /api/orders/` - View user orders

## Testing
Run the tests using the following command:
```bash
python manage.py test
```


## Future Enhancements
- Payment gateway integration.
- Order tracking system.
- Enhanced analytics and reporting for administrators.


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Contact
For any inquiries or support, feel free to contact:
- **Developer**: Md Mehedi Hasan Raj
- **Email**: [mehedihasanraj007@gmail.com]

## Git Repository
Find the code here: [GitHub Repository Link]([<repository-url>](https://github.com/MehediHasanRaj/Subway_Management_System))
