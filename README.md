# UniTrade – University Marketplace Web Application

# COMPSCI5012 Internet Technology Coursework

University of Glasgow

---

## Live Deployment

The application is fully deployed using Render:

https://it-team-dj.onrender.com

This deployed version represents the final production-ready system, including UI optimisation, static asset handling, and cloud-based media storage.

---

## Project Overview

UniTrade is a full-stack web-based marketplace platform designed for university students to buy and sell second-hand items in an efficient, user-friendly, and visually enhanced environment.

The system supports the complete user journey from browsing listings to managing purchases and interactions.

---

## Key Features

### User Authentication

Secure registration, login, and logout using Django’s built-in authentication system.

### Marketplace Listings

Users can create listings including:

* title
* description
* price
* category
* image upload (Cloudinary integration)

### Search and Filtering

Interactive search functionality improves discoverability and usability.

### Favourites System

Users can save items to a personal favourites list.

### Cart System

Users can add items to a cart before purchase.

### Comment System

Users can leave comments on item listings.

### Address Management

Users can manage delivery addresses through the account dashboard.

---

## UI and UX Design

The interface was refined to improve usability, clarity, and visual hierarchy.

Enhancements include:

* High-quality hero section with background imagery
* Improved spacing, typography, and contrast
* Interactive hover effects on item cards
* Clear call-to-action buttons
* Responsive design for multiple screen sizes

These improvements enhance user experience without compromising performance.

---

## System Architecture

The project follows Django’s Model–View–Template (MVT) architecture:

* Models define database structure
* Views handle business logic
* Templates manage presentation

The system is organised into modular Django apps:

| App      | Responsibility                           |
| -------- | ---------------------------------------- |
| items    | marketplace item management              |
| cart     | shopping cart functionality              |
| comments | item comments                            |
| users    | account dashboard and address management |
| accounts | authentication and registration          |

---

## Project Structure

```
IT-team-DJ
│
├── items/
├── cart/
├── comments/
├── users/
├── accounts/
├── templates/
├── static/
├── media/
├── report-assets/
├── config/
├── manage.py
└── requirements.txt
```

---

## Technologies Used

### Backend

* Python
* Django
* Django ORM
* PostgreSQL (production)

### Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

### Deployment and Tools

* Render (deployment)
* Cloudinary (media storage)
* WhiteNoise (static file handling)
* GitHub (version control)
* Chrome DevTools & Lighthouse (evaluation)

---

## Installation and Setup

```bash
git clone https://github.com/ChipsZzz/IT-team-DJ
cd IT-team-DJ
```

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

```bash
python manage.py migrate
python manage.py runserver
```

Open in browser:

http://127.0.0.1:8000

---

## Testing

Run backend tests:

```bash
python manage.py test
```

The test suite verifies:

* model behaviour
* view responses
* cart functionality
* comment system
* authentication protection

---

## Accessibility and Performance

The system was evaluated using Google Lighthouse.

| Page        | Performance | Accessibility | Best Practices | SEO |
| ----------- | ----------- | ------------- | -------------- | --- |
| Homepage    | 100         | 82            | 100            | 82  |
| Marketplace | 100         | 73            | 100            | 82  |

These results demonstrate that UI improvements enhanced usability while maintaining strong technical performance.

---

## Evaluation Evidence

Supporting evaluation materials are included in:

```
report-assets/lighthouse/test/
```

This folder contains:

* Lighthouse screenshots for multiple pages
* Item detail performance results
* Backend unit test evidence

These assets provide verifiable proof of system performance and correctness.

---

## Deployment Notes

The system is fully production-ready:

* Static files served using WhiteNoise
* Media files hosted via Cloudinary
* Environment variables used for secure configuration
* Database automatically configured for local and deployed environments

---

## Future Improvements

* Payment integration
* Messaging system
* Advanced filtering and sorting
* Recommendation system

---

## Authors

Team DJ

Zhen Liu – 3149144L
Zhenyu Wang – 3075222W
Tianxin Han – 3047131H

University of Glasgow
COMPSCI5012 Internet Technology Coursework
