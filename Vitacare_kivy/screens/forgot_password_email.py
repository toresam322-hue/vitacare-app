from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivy.app import App
import requests

class ForgotPasswordEmailScreen(Screen):
    def on_pre_enter(self):
        self.ids.email_input.text = ""

    def send_reset_code(self, email):
        email = email.strip()
        if not email:
            toast("Email is required.")
            return

        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/users/forgot-password/",
                json={"email": email},
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                if data.get("redirect") == "signup":
                    toast("Email not registered. Please sign up first.")
                    self.manager.current = "sign_up"
                else:
                    toast("Reset code sent. Check your email.")
                    App.get_running_app().email_for_reset = email
                    self.manager.current = "forgot_password_code"
            else:
                toast(f"Failed to send reset code: {response.text}")
        except requests.exceptions.RequestException as e:
            toast(f"Network error: {e}")