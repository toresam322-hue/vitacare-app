from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import requests

class BookAppointmentScreen(Screen):

    def on_enter(self):
        self.get_latest_appointment()

    def show_popup(self, message):
        popup = Popup(title='Appointment Info',
                      content=Label(text=message),
                      size_hint=(0.8, 0.4))
        popup.open()

    def get_latest_appointment(self):
        token = self.manager.access_token
        headers = {"Authorization": f"Bearer {token}"}
        try:
            url = "http://127.0.0.1:8000/api/appointments/my-latest/"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                result = response.json()
                doctor = result.get("doctor_name")
                date = result.get("date")
                time = result.get("time")
                self.ids.appointment_status.text = f"You have an appointment with {doctor} on {date} at {time}"
            else:
                self.ids.appointment_status.text = "No appointments found"
        except Exception:
            self.ids.appointment_status.text = "Failed to load appointments"

    def book_appointment(self):
        email = self.ids.doctor_email.text.strip()
        date = self.ids.date_input.text.strip()
        time = self.ids.time_input.text.strip()

        if not email:
            self.show_popup("Doctor email is required")
            return

        try:
            # ✅ FIXED URL
            headers = {"Authorization": f"Bearer {self.manager.access_token}"}
            doctor_resp = requests.get("http://127.0.0.1:8000/api/users/doctor-id/?email=" + email, headers=headers)
            #
            if doctor_resp.status_code == 200:
                doctor_id = doctor_resp.json().get("doctor_id")
            else:
                self.show_popup("Doctor not found")
                return

            data = {"doctor": doctor_id}
            if date:
                data["date"] = date
            if time:
                data["time"] = time

            url = "http://127.0.0.1:8000/api/appointments/book/"
            #headers = {"Authorization": f"Bearer {self.manager.access_token}"}
            response = requests.post(url, json=data, headers=headers)

            if response.status_code == 201:
                self.show_popup("Appointment booked successfully")
                self.get_latest_appointment()
            else:
                msg = response.json().get("error") or str(response.content)
                self.show_popup(f"Booking failed: {msg}")

        except Exception as e:
            self.show_popup(str(e))