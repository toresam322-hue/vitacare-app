from kivy.uix.screenmanager import Screen
import requests

class PatientHomeScreen(Screen):
    def on_pre_enter(self, *args):
        """
        Runs when the patient home screen is about to be displayed.
        Loads the latest appointment and sets a welcome label.
        """
        user_data = self.manager.get_screen('patient_login').user_data if hasattr(self.manager.get_screen('patient_login'), 'user_data') else None
        if user_data:
            name = user_data.get('first_name', 'User')
            self.ids.welcome_label.text = f"Welcome {name}!"
        else:
            self.ids.welcome_label.text = "Welcome!"

        self.load_appointment()

    def logout(self):
        """
        Logs out the user and clears token/session info.
        """
        self.manager.access_token = None
        self.manager.refresh_token = None
        self.manager.current = 'patient_login'

        login_screen = self.manager.get_screen('patient_login')
        login_screen.clear_fields()

    def load_appointment(self):
        """
        Loads the patient's latest appointment from the backend
        and displays it in the UI.
        """
        token = self.manager.access_token
        headers = {"Authorization": f"Bearer {token}"}
        url = "http://127.0.0.1:8000/api/appointments/my-latest/"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                doctor = data.get("doctor_name")
                date = data.get("date")
                time = data.get("time")
                self.ids.appointment_label.text = f"You have an appointment with Dr. {doctor} on {date} at {time}"
            elif response.status_code == 204:
                self.ids.appointment_label.text = "No appointments"
            else:
                self.ids.appointment_label.text = "Unable to load appointment"
        except Exception as e:
            self.ids.appointment_label.text = "Failed to load appointments"