from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.main_menu import MainMenuScreen
from screens.result_screen import ResultScreen


class PigmentaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(ResultScreen(name='result_screen'))
        return sm


if __name__ == '__main__':
    PigmentaApp().run()