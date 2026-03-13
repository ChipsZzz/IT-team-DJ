# UniTrade – University Marketplace Web Application
COMPSCI5012 ITECH Coursework – University of Glasgow

## Project Overview

UniTrade is a web-based marketplace platform designed for university students to buy and sell second-hand items. The application allows users to list items for sale, browse listings, manage personal accounts, and interact with other users through features such as favourites, comments, and cart functionality.

The system is implemented using the Django web framework and follows a modular architecture that separates functionality into reusable applications.

---

## Key Features

### User Authentication
Users can register, log in, and log out using Django’s built-in authentication system.

### Marketplace Listings
Users can create listings including title, description, price, and images.

### Search and Filtering
Users can browse and search for items in the marketplace.

### Favourites System
Users can mark items as favourites to easily access them later.

### Cart System
Users can add items to a cart before purchasing.

### Comment System
Users can leave comments on item listings.

### Address Management
Users can manage their delivery address through the account dashboard.

### Responsive Design
The interface uses Bootstrap to support desktop and mobile layouts.

---

## System Architecture

The project follows Django’s Model–View–Template (MVT) architecture.

- Models define database structure.
- Views handle business logic.
- Templates manage presentation.

The system is organised into multiple Django apps:

| App | Responsibility |
|----|----|
items | marketplace item management |
cart | cart functionality |
users | account dashboard and address management |
accounts | authentication and registration |
comments | item comments |

---

## Technologies Used

Backend:
- Python
- Django
- Django ORM
- SQLite

Frontend:
- HTML
- CSS
- Bootstrap
- JavaScript

Development Tools:
- Visual Studio Code
- Git and GitHub
- Chrome DevTools (Lighthouse)

---

## Installation and Setup

Clone the repository:

```bash
git clone <repository-url>
cd UniTrade
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

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## Running Unit Tests

Run tests using Django’s testing framework:

```bash
python manage.py test
```

Django automatically creates a temporary test database and removes it after testing.

The project currently includes tests for:

- Item model
- Address model

---

## Accessibility

Accessibility was evaluated using Google Lighthouse.

The application follows accessibility practices such as:

- semantic HTML
- labelled form fields
- readable layout and contrast

Accessibility scores range between **73 and 82** across tested pages.

---

## Sustainability and Performance

Performance was evaluated using Google Lighthouse.

| Page | Performance | Accessibility | Best Practices | SEO |
|----|----|----|----|----|
Homepage | 100 | 79–82 | 100 | 82 |
Marketplace | 100 | 73 | 100 | 82 |

The application achieves excellent performance due to efficient resource loading and lightweight design.

---

## Future Improvements

Potential improvements include:

- payment integration
- advanced search filters
- messaging between buyers and sellers
- recommendation systems

---

## Author

Team DJ
Zhen Liu 3149144L
Zhenyu Wang 3075222W
Tianxin Han 3047131H
University of Glasgow  
COMPSCI5012 Internet Technology Coursework Project