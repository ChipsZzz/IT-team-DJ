# UniTrade – University Marketplace Web Application

# COMPSCI5012 Internet Technology Coursework

University of Glasgow

---

## 🌐 Live Deployment

The application is fully deployed using Render:

https://it-team-dj.onrender.com

This deployed version represents the final production-ready system, including UI optimisation, static asset handling, and cloud-based media storage.

---

## 📌 Project Overview

UniTrade is a full-stack web-based marketplace platform designed for university students to buy and sell second-hand items in an efficient, user-friendly, and visually enhanced environment.

The system supports the complete user journey, including browsing, purchasing, selling, and managing items.

---

## 🚀 Key Features

### 🔐 User Authentication

Secure registration, login, and logout using Django’s built-in authentication system.

---

### 🛍 Marketplace Listings

Users can create listings including:

* title
* description
* price
* category
* image upload (Cloudinary integration)

---

### 🔎 Search and Category Filtering

* Keyword-based search
* Category filtering (Books, Electronics, Fashion, Bikes, Gaming, Phones)
* Displays "No items found" when category is empty

---

### ❤️ Favourites System

Users can save items to a personal favourites list.

---

### 🛒 Cart and Purchase System

* Add items to cart
* Complete purchase flow
* Purchase history tracking

---

### 🔄 Return System

* Users can return purchased items
* Returned items are displayed in history
* Improves realism of marketplace workflow

---

### 💬 Comment System

Users can leave comments on item listings.

---

### 📦 Sales & Purchase Dashboard

Users can view:

* My Purchases
* My Sales
* Returned Items

---

### 📍 Address Management

Users can manage delivery addresses through the account dashboard.

---

## 🎨 UI and UX Design

The interface was refined to improve usability, clarity, and visual hierarchy.

Enhancements include:

* High-quality hero section with background imagery
* Interactive category navigation
* Clean card-based layout
* Smooth hover animations
* Clear call-to-action buttons
* Responsive design for all screen sizes

These improvements enhance user experience while maintaining strong performance.

---

## 🏗 System Architecture

The project follows Django’s Model–View–Template (MVT) architecture:

* Models → database structure
* Views → business logic
* Templates → UI rendering

### 📦 Modular App Structure

| App      | Responsibility                           |
| -------- | ---------------------------------------- |
| items    | marketplace item management              |
| cart     | shopping cart and purchasing             |
| comments | item comments                            |
| users    | account dashboard and address management |
| accounts | authentication and registration          |

---

## 📂 Project Structure

IT-team-DJ

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

---

## ⚙️ Technologies Used

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

### Deployment & Tools

* Render (deployment)
* Cloudinary (media storage)
* WhiteNoise (static file handling)
* GitHub (version control)
* Chrome DevTools & Lighthouse (evaluation)

---

## 🧪 Installation and Setup

git clone https://github.com/ChipsZzz/IT-team-DJ
cd IT-team-DJ

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

Open in browser:

http://127.0.0.1:8000

---

## 🧪 Testing

python manage.py test

The test suite verifies:

* model behaviour
* view responses
* cart functionality
* comment system
* authentication protection

---

## 📊 Accessibility and Performance

The system was evaluated using Google Lighthouse on the deployed version.

| Page        | Performance | Accessibility | Best Practices | SEO |
| ----------- | ----------- | ------------- | -------------- | --- |
| Homepage    | 93          | 78            | 100            | 82  |
| Marketplace | 99          | 71            | 100            | 82  |

These results indicate strong performance and compliance with modern web standards.
Minor accessibility improvements remain possible but do not impact core usability.

---

## 📸 Evaluation Evidence

Supporting evaluation materials are included in:

report-assets/lighthouse/test/

This folder contains:

* Lighthouse screenshots
* Performance analysis results
* System validation evidence

---

## 🚀 Deployment Notes

The system is fully production-ready:

* Static files served using WhiteNoise
* Media files hosted via Cloudinary
* Environment variables for secure configuration
* Database auto-configured for local and deployed environments

---

## 🔮 Future Improvements

* Online payment integration
* Real-time messaging system
* Advanced filtering and sorting
* AI-based recommendation system

---

## 👨‍💻 Authors

Team DJ

Zhen Liu – 3149144L
Zhenyu Wang – 3075222W
Tianxin Han – 3047131H

University of Glasgow
COMPSCI5012 Internet Technology Coursework
