# 🏥 Clinic API — Django REST Framework

> Developed as part of a technical assessment.  
This project implements a **Clinic Management REST API** using Django and Django REST Framework (DRF), covering authentication, filtering, validation, and analytics.

---

## 🧩 Project Structure

```
clinic_api/
│
├── clinic_api/
│   ├── settings.py
│   ├── urls.py
│
├── patients/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── permissions.py
│   └── admin.py
│
└── manage.py
```

---

## 🚀 Features

- Patient & Appointment Management  
- ForeignKey relationship  
- Search & filtering support  
- Custom input validation  
- ORM-based analytics endpoints  
- Token Authentication  
- Role-based access control (Staff vs Non-Staff)  
- Consistent API response format  

---

## ⚙️ Installation

```
# Clone Repository
git clone https://github.com/iamdeepaksaxena/Technical-Assesment.git

# Create Virtual Environment
python -m venv venv
venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run Migrations
python manage.py makemigrations
python manage.py migrate

# Create Superuser
python manage.py createsuperuser

# Run Server
python manage.py runserver
```

---

## 🧩 SECTION 01 — Models & Admin

### Patient Model
- name  
- age  
- gender  
- contact_number  
- blood_group  
- created_at  

### Appointment Model
- doctor_name  
- appointment_date  
- reason  
- status (Pending / Confirmed / Cancelled)  
- Linked with Patient (ForeignKey)

---

### Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

## 🚀 SECTION 02 — DRF APIs

### Patient CRUD

```
GET    /api/patients/
POST   /api/patients/
GET    /api/patients/<id>/
PUT    /api/patients/<id>/
DELETE /api/patients/<id>/
```

---

### Appointment APIs

```
GET /api/appointments/
GET /api/appointments/?status=Pending
GET /api/appointments/?patient_id=1
```

---

### Validation

- Age must be between 0–120  
- Contact number must be exactly 10 digits  

---

## 📊 SECTION 03 — ORM Queries

### Stats Endpoint

```
GET /api/stats/
```

Returns:
- Total patients  
- Total appointments  
- Count by status  

---

### Upcoming Appointments

```
GET /api/appointments/upcoming/
```

- Next 7 days  
- Ordered by date  

---

### Search

```
GET /api/patients/?search=rahul
```

---

## 🔐 SECTION 04 — Authentication & Permissions

### Login API

```
POST /api/auth/login/
```

Response:

```json
{
  "success": true,
  "token": "abc123..."
}
```

---

### Permissions

- Non-Staff → Read Only  
- Staff → Full Access  

---

### Response Format

```json
{
  "success": true/false,
  "data": ...,
  "message": "..."
}
```

---

## 🌐 API Endpoints

```
http://127.0.0.1:8000/api/
http://127.0.0.1:8000/api/patients/
http://127.0.0.1:8000/api/appointments/
http://127.0.0.1:8000/api/stats/
http://127.0.0.1:8000/api/appointments/upcoming/
```

---


## Thank You Sir/Ma'am
