from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("./Section27/design.kv")

class LoginScreen(Screen):

    def sign_up(self):
        print("sign up")
        self.manager.current = "sign_up_screen"

class SignUpScreen(Screen):
    
    def add_user(self, uname, pword):
        print(uname, pword)


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
    
if __name__ == "__main__":
    MainApp().run()