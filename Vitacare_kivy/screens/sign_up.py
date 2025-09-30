from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import requests

class SignUpScreen(Screen):
    def on_pre_enter(self):
        # Clear all input fields
        self.ids.email_input.text = ""
        self.ids.first_name_input.text = ""
        self.ids.last_name_input.text = ""
        self.ids.phone_input.text = ""
        self.ids.address_input.text = ""
        self.ids.password_input.text = ""
        self.ids.confirm_password_input.text = ""

    def sign_up(self):
        email = self.ids.email_input.text.strip()
        first_name = self.ids.first_name_input.text.strip()
        last_name = self.ids.last_name_input.text.strip()
        phone = self.ids.phone_input.text.strip()
        address = self.ids.address_input.text.strip()
        password = self.ids.password_input.text
        confirm_password = self.ids.confirm_password_input.text

        if password != confirm_password:
            self.show_popup("Error", "Passwords do not match")
            return

        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "address": address,
            "password": password,
            "confirm_password": confirm_password
        }

        try:
            response = requests.post("http://127.0.0.1:8000/api/users/register/", json=data, timeout=5)
            if response.status_code == 201:
                self.show_popup("Success", "Registration successful!")
                self.manager.current = "patient_login"
            else:
                try:
                    error_msg = response.json()
                except ValueError:
                    error_msg = response.text
                self.show_popup("Registration Failed", str(error_msg))
        except requests.exceptions.RequestException as e:
            self.show_popup("Network Error", str(e))

    def show_popup(self, title, message):
        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(None, None),
            size=(320, 180)
        )
        popup.open()