from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import requests
from kivy.clock import Clock

class DoctorLoginScreen(Screen):
    def clear_fields(self):
        self.ids.email_input.text = ''
        self.ids.license_input.text = ''
        self.ids.password_input.text = ''

    def show_popup(self, message):
        popup = Popup(title='Login Info', content=Label(text=message),
                      size_hint=(0.8, 0.4))
        popup.open()

    def login_doctor(self):
        email = self.ids.email_input.text.strip()
        license_num = self.ids.license_input.text.strip()
        password = self.ids.password_input.text.strip()

        if not email or not license_num or not password:
            self.show_popup("All fields are required.")
            return

        try:
            url = "http://127.0.0.1:8000/api/users/doctor/login/"
            data = {
                "email": email,
                "license": license_num,
                "password": password
            }
            response = requests.post(url, json=data)

            if response.status_code == 200:
                result = response.json()
                self.manager.access_token = result.get("access")
                self.manager.refresh_token = result.get("refresh")
                doctor_name = result['doctor']['name']
                self.manager.current = 'doctor_home'

                def set_label(dt):
                    self.manager.get_screen('doctor_home').ids.welcome_label.text = f"Welcome, {doctor_name}"

                Clock.schedule_once(set_label, 0.5)
            else:
                self.show_popup("Login failed. Check credentials.")
        except Exception as e:
            self.show_popup(str(e))