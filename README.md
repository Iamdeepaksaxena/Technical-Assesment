🏥 Clinic API — Django REST Framework

Developed as part of a technical assessment.
This project implements a Clinic Management REST API using Django and Django REST Framework (DRF), covering end-to-end backend development including authentication, filtering, validation, and analytics.

🧩 Project Structure
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
🚀 Features
🧑‍⚕️ Patient & Appointment Management
🔗 ForeignKey relationship between models
🔍 Search & filtering support
✅ Custom input validation
📊 ORM-based analytics endpoints
🔐 Token-based authentication
🛡 Role-based access control (Staff vs Non-Staff)
📦 Consistent API response format
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/clinic_api.git

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Run Server
python manage.py runserver
🧩 SECTION 01 — Models & Admin
✅ Patient Model
name
age
gender
contact_number
blood_group
created_at
✅ Appointment Model
doctor_name
appointment_date
reason
status (Pending / Confirmed / Cancelled)
Linked to Patient using ForeignKey
🛠 Admin Panel

Access:

http://127.0.0.1:8000/admin/

✔ Add Patients
✔ Add Appointments
✔ Manage records easily

🚀 SECTION 02 — DRF APIs
✅ Patient CRUD
GET    /api/patients/
POST   /api/patients/
GET    /api/patients/<id>/
PUT    /api/patients/<id>/
DELETE /api/patients/<id>/
✅ Appointment APIs with Filtering
GET /api/appointments/
GET /api/appointments/?status=Pending
GET /api/appointments/?patient_id=1
✅ Input Validation
Age must be between 0–120
Contact number must be exactly 10 digits
📊 SECTION 03 — ORM Queries
✅ Stats Endpoint
GET /api/stats/

Returns:

Total patients
Total appointments
Count of appointments by status
✅ Upcoming Appointments
GET /api/appointments/upcoming/

✔ Returns appointments for next 7 days
✔ Ordered by appointment_date

🔍 Search Patients
GET /api/patients/?search=rahul

✔ Case-insensitive search using icontains

🔐 SECTION 04 — Authentication & Permissions
✅ Token Authentication
🔹 Login API
POST /api/auth/login/
Response
{
  "success": true,
  "token": "abc123..."
}
🛡 Custom Permission
User Type	Access
👤 Non-Staff	Read Only (GET)
🛠 Staff	Full Access
📦 Consistent Response Format
{
  "success": true/false,
  "data": ...,
  "message": "..."
}
🌐 API Endpoints
API Root:
http://127.0.0.1:8000/api/

Patients:
http://127.0.0.1:8000/api/patients/

Appointments:
http://127.0.0.1:8000/api/appointments/

Stats:
http://127.0.0.1:8000/api/stats/

Upcoming:
http://127.0.0.1:8000/api/appointments/upcoming/
