from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock
import requests
import json

class PatientLoginScreen(Screen):
    def clear_fields(self):
        self.ids.email_input.text = ''
        self.ids.password_input.text = ''
        
    def on_pre_enter(self):
        self.clear_fields()

    def show_popup(self, message):
        popup = Popup(title='Login Info', content=Label(text=message),
                      size_hint=(0.8, 0.4))
        popup.open()

    def login_user(self):
        email = self.ids.email_input.text.strip()
        password = self.ids.password_input.text.strip()

        if not email or not password:
            self.show_popup("All fields are required.")
            return

        try:
            url = "http://127.0.0.1:8000/api/users/login/"
            data = {
                "email": email,
                "password": password
            }
            response = requests.post(url, json=data)

            if response.status_code == 200:
                result = response.json()
                access_token = result.get('access')
                refresh_token = result.get('refresh')

                # Store tokens for future use
                self.manager.access_token = access_token
                self.manager.refresh_token = refresh_token

                # Now request /me/ using access token
                headers = {"Authorization": f"Bearer {access_token}"}
                me_response = requests.get("http://127.0.0.1:8000/api/users/me/", headers=headers)

                if me_response.status_code == 200:
                    user_data = me_response.json()
                    first_name = user_data.get("first_name", "")
                    self.manager.current = 'patient_home'
                    
                    # Wait for screen switch before setting label
                    def update_label(dt):
                        self.manager.get_screen('patient_home').ids.welcome_label.text = f"Welcome, {first_name}!"

                    Clock.schedule_once(update_label, 0.5)

                else:
                    self.show_popup("Failed to fetch user info.")
            else:
                self.show_popup("Invalid email or password.")
        except Exception as e:
            self.show_popup("Error: " + str(e))