from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivy.app import App
import requests

class ForgotPasswordCodeScreen(Screen):
    def on_pre_enter(self):
        self.ids.code_input.text = ""

    def verify_code(self):
        app = App.get_running_app()
        email = getattr(app, 'email_for_reset', '')
        code = self.ids.code_input.text.strip()

        if not email:
            toast("Email not found. Please request reset code again.")
            self.manager.current = 'forgot_password_email'
            return

        if not code or len(code) != 5 or not code.isdigit():
            toast("Please enter a valid 5-digit code.")
            return

        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/users/verify-code/",
                json={'email': email, 'code': code},
                timeout=5
            )
            if response.status_code == 200:
                toast("Code verified! Please reset your password.")
                self.manager.current = 'reset_password'
            else:
                toast("Invalid or expired code.")
        except requests.exceptions.RequestException as e:
            toast(f"Error verifying code: {e}")