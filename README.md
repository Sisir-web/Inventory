<<<<<<< HEAD
# Police Department Item Allocation and Tracking System

This is a Django-based web application designed to manage and track the allocation of government-issued items (such as boots, belts, caps, and uniforms) to police personnel across different units.

## 📚 Project Overview

The system allows unit-wise admin control, where each admin handles item distribution and tracking for their own unit. The project includes an integrated AI chatbot for user queries and uses Django’s default SQLite database for data management.

---

## ✅ Key Features

- **Unit-based Admin Panels**:  
  Three admin groups (Unit A, Unit B, Unit C) manage their own employees and allocations.
  
- **Item Allocation Tracking**:  
  Track and record distribution of items provided by the government.

- **Role-Based Access Control**:  
  Admins only see and manage employees and data specific to their unit.

- **AI Chatbot Integration**:  
  Helps answer common queries for users.

- **Simple and Lightweight**:  
  Uses Django’s default SQLite database, perfect for quick deployment and testing.

---

## 🛠 Technologies Used

- Django (Python)
- SQLite (Django default database)
- HTML/CSS/Bootstrap (frontend)
- Django Admin with custom filtering
- Django Groups & Permissions for role-based access

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

1.Create a virtual environment & activate
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

2.Apply migrations
python manage.py migrate

3.Create superuser
python manage.py createsuperuser

4.Run the server
python manage.py runserver



=======
# Inventory
A Django-based web application designed to manage and track the distribution of government-issued items (such as boots, belts, caps, and uniforms) to police personnel.  The system features role-based admin panels, where each admin can only manage employees and allocations for their respective units. 
>>>>>>> 95807ae (Initial commit)
