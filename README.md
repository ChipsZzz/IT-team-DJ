# UniTrade – University Marketplace Web Application

COMPSCI5012 Internet Technology Coursework  
University of Glasgow

---

## Live Deployment

The application is deployed online using Render.

Live website:

https://it-team-dj.onrender.com

---

## Project Overview

UniTrade is a web-based marketplace platform designed for university students to buy and sell second-hand items.

The system allows users to:

- create item listings
- browse marketplace listings
- search and filter items
- save favourite items
- add items to a cart
- leave comments on item listings
- manage account information and delivery addresses

The application is built using the Django web framework and follows a modular architecture where functionality is separated into reusable apps.

---

## Key Features

### User Authentication
Users can register, log in, and log out using Django’s built-in authentication system.

### Marketplace Listings
Users can create listings including:

- title
- description
- price
- category
- item image

### Search and Filtering
Users can search and filter items using front-end JavaScript interaction.

### Favourites System
Users can save items to a personal favourites list.

### Cart System
Users can add items to a cart before purchasing.

### Comment System
Users can leave comments on item listings.

### Address Management
Users can manage delivery addresses through the account dashboard.

### Responsive Design
The interface uses Bootstrap to support both desktop and mobile layouts.

---

## System Architecture

The project follows Django’s Model–View–Template (MVT) architecture.

- Models define database structure
- Views handle business logic
- Templates manage presentation

The project is organised into several Django apps:

| App | Responsibility |
|----|----|
items | marketplace item management |
cart | shopping cart functionality |
comments | item comments |
users | account dashboard and address management |
accounts | authentication and registration |

---

## Project Structure

```
IT-team-DJ
│
├── items/          # marketplace item management
├── cart/           # cart functionality
├── comments/       # comment system
├── users/          # account dashboard and address
├── accounts/       # authentication and registration
├── templates/      # global templates
├── media/          # uploaded item images
├── config/         # Django settings
├── manage.py
└── requirements.txt
```

---

## Technologies Used

### Backend

- Python
- Django
- Django ORM
- SQLite

### Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

### Development Tools

- Visual Studio Code
- Git and GitHub
- Chrome DevTools
- Lighthouse

---

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/ChipsZzz/IT-team-DJ
cd IT-team-DJ
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment (Windows):

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open the site in a browser:

```
http://127.0.0.1:8000
```

---

## Running Unit Tests

Backend functionality is tested using Django’s built-in testing framework.

Run the test suite using:

```bash
python manage.py test
```

The tests verify core backend components including:

- Item model behaviour
- Item view responses
- Cart functionality
- Comment system logic
- Authentication protection

Example test output:

```
Found 12 tests
Ran 12 tests
OK
```

Django automatically creates a temporary test database and removes it after testing.

---

## Accessibility

Accessibility was evaluated using Google Lighthouse.

The application follows accessibility practices such as:

- semantic HTML structure
- labelled form fields
- readable layout and colour contrast

Accessibility scores range between **73 and 82** across tested pages.

---

## Performance and Sustainability

Performance analysis was conducted using Lighthouse.

| Page | Performance | Accessibility | Best Practices | SEO |
|----|----|----|----|----|
Homepage | 100 | 79–82 | 100 | 82 |
Marketplace | 100 | 73 | 100 | 82 |

The application achieves strong performance due to lightweight assets and efficient page rendering.

---

## Future Improvements

Potential improvements include:

- payment integration
- messaging between buyers and sellers
- advanced search filters
- recommendation systems

---

## Authors

Team DJ

Zhen Liu – 3149144L  
Zhenyu Wang – 3075222W  
Tianxin Han – 3047131H  

University of Glasgow  
COMPSCI5012 Internet Technology Coursework