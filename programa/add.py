from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Main(Screen):
    def __init__(self,**kworks):
        super().__init__(**kworks)
        but = Button(text = "OK")
        text_int = TextInput(multiline = False)
        v1 = BoxLayout(orientation = "vertical")
        v1.add_widget(but)
        v1.add_widget(text_int)

        self.add_widget(v1)

        but.on_press = self.next

    def next(self):
        self.manager.transition.direction = "up"
        self.manager.current = "second"
        
class Main2(Screen):
    def __init__(self,**kworks):
        super().__init__(**kworks)
        but = Button(text = "OK2")

        self.add_widget(but)
        but.on_press = self.next

    def next(self):
        self.manager.transition.direction = "down"
        self.manager.current = "first"

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main(name = "first"))
        sm.add_widget(Main2(name = "second"))

        return sm
    

app = MyApp()
app.run()



