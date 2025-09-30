from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class DoctorHomeScreen(Screen):
    def show_popup(self, message):
        popup = Popup(title='Info', content=Label(text=message),
                      size_hint=(0.8, 0.4))
        popup.open()

    def view_appointments(self):
        self.show_popup("Appointments feature coming soon.")

    def view_patient_history(self):
        self.show_popup("Patient history feature coming soon.")

    def prescribe_medication(self):
        self.show_popup("Prescribe medication feature coming soon.")

    def chat_with_patient(self):
        self.show_popup("Chat feature coming soon.")

    def start_video_call(self):
        self.show_popup("Video call feature coming soon.")