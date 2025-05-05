import glob
from pathlib import Path
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file("./Section27/design.kv")

class LoginScreen(Screen):

    def sign_up(self):
        print("sign up")
        self.manager.current = "sign_up_screen"
    
    def login(self, uname, pword):
        with open("./Section27/user.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "login_screen_success"
            self.ids.login_wrong.text = ""
        else:
            self.ids.login_wrong.text = "Wrong name of password"


class SignUpScreen(Screen):
    
    def add_user(self, uname, pword):
        print(uname, pword)
        with open("./Section27/user.json") as file:
            users = json.load(file)
         
        users[uname] = {"username":uname, "password":pword, "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S") }

        with open("./Section27/user.json", "w") as file:
            json.dump(users, file)
        
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction ='right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("./Section27/quotes/*txt")

        available_feelings = [Path(filename).stem for filename in available_feelings]
        if feel in available_feelings:
            with open(f"./Section27/quotes/{feel}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            print(quotes)
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"

class ImageButton(HoverBehavior,Image, ButtonBehavior):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
    
if __name__ == "__main__":
    MainApp().run()