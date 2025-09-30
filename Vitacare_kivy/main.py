from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

# Import screens
from screens.welcome import WelcomeScreen
from screens.patient_login import PatientLoginScreen
from screens.doctor_login import DoctorLoginScreen
from screens.sign_up import SignUpScreen
from screens.patient_home import PatientHomeScreen
from screens.doctor_home import DoctorHomeScreen
from screens.forgot_password_email import ForgotPasswordEmailScreen
from screens.forgot_password_code import ForgotPasswordCodeScreen
from screens.reset_password import ResetPasswordScreen
from screens.book_appointment import BookAppointmentScreen

# Load all .kv files
Builder.load_file("kv/welcome_screen.kv")
Builder.load_file("kv/patient_login.kv")
Builder.load_file("kv/doctor_login.kv")
Builder.load_file("kv/sign_up.kv")
Builder.load_file("kv/patient_home.kv")
Builder.load_file("kv/doctor_home.kv")
Builder.load_file("kv/forgot_password_email.kv")
Builder.load_file("kv/forgot_password_code.kv")
Builder.load_file("kv/reset_password.kv")
Builder.load_file("kv/book_appointment.kv")  # ✅ Important fix

class VitaCareApp(MDApp):
    def build(self):
        self.email_for_reset = ""
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name="welcome"))
        sm.add_widget(PatientLoginScreen(name="patient_login"))
        sm.add_widget(DoctorLoginScreen(name="doctor_login"))
        sm.add_widget(SignUpScreen(name="sign_up"))
        sm.add_widget(PatientHomeScreen(name="patient_home"))
        sm.add_widget(DoctorHomeScreen(name="doctor_home"))
        sm.add_widget(ForgotPasswordEmailScreen(name="forgot_password_email"))
        sm.add_widget(ForgotPasswordCodeScreen(name="forgot_password_code"))
        sm.add_widget(ResetPasswordScreen(name="reset_password"))
        sm.add_widget(BookAppointmentScreen(name="book_appointment"))  # ✅ Added correctly

        return sm

if __name__ == "__main__":
    VitaCareApp().run()