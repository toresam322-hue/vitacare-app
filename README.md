VitaCare Telemedicine App
A full-stack telemedicine platform built with Django (backend) and Kivy/KivyMD (mobile frontend).
The app allows patients and doctors to connect through appointments, chat, prescriptions, and video calls.
Features:
1)Patient:
Signup, Login, Forgot Password
 Book and manage appointments
View prescriptions
Chat with doctors
 Video call with doctors
 Access past consultations
 2)Doctor:
Secure login with license number
 View upcoming appointments
 Prescribe medication
View patient history
Chat with patients
Video calls with patients
Tech Stack

Frontend (Mobile): Kivy, KivyMD, Python
Backend (API): Django, Django REST Framework
Authentication: JWT (djangorestframework-simplejwt)
Database: PostgreSQL (or SQLite for local dev)
Real-time Chat: Firebase / Django Channels (planned)
Video Calls: WebRTC (planned)
 
Project Structure:
VitaCare-App/
 ├── VitaCare_backend/   # Django backend (APIs, models, JWT, appointments, users, doctors)
 ├── VitaCare_kivy/      # Kivy frontend (screens, kv files, navigation, API calls)
 └── README.md           # Project documentation

Setup Instructions:
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/VitaCare-App.git
cd VitaCare-App
 2. Setup Backend (Django)
cd VitaCare_backend
python -m venv env
source env/bin/activate  # (Linux/Mac)
env\Scripts\activate     # (Windows)

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Backend runs at:  http://127.0.0.1:8000/
3. Setup Frontend (Kivy)
cd ../VitaCare_kivy
pip install -r requirements.txt
python main.py
Kivy app launches locally.

Example Test Flow: 
Register/Login as a Patient.
Manually register Doctors in Django Admin.
Book an appointment → System suggests next available slot.
View appointment status on Patient Home.
Doctor can login → See upcoming appointments.
(Planned) Start chat or video call.

Next Steps:
Implement real-time chat with Firebase/Django Channels
Add video conferencing with WebRTC
Improve appointment calendar UI
Add push notifications
 
License:
This project is licensed under the MIT License.
