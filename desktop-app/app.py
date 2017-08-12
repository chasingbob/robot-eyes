import datetime

import kivy
kivy.require('1.10.0') 

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.core.window import Window

Builder.load_file('app.kv')

class TimeWidget(Widget):
    time = StringProperty('time')
    date = StringProperty('date')

    def update(self, *args):
        self.date = datetime.date.today().strftime("%A, %d %B %Y")
        self.time = datetime.datetime.now().strftime("%H:%M")

class Container(FloatLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

        anchor_tr = AnchorLayout(anchor_x='right', anchor_y='top', size_hint=(1,1))
        tw = TimeWidget()
        tw.update()
        Clock.schedule_interval(tw.update,6)
        anchor_tr.add_widget(tw)
        self.add_widget(anchor_tr)

        anchor_ml = AnchorLayout(anchor_x='left', anchor_y='center', size_hint=(1,1))
        btn1 = Button(text='Load class A')
        btn1.bind(on_press=self.LoadClassA)
    
        btn2 = Button(text='Load class B')
        btn2.bind(on_press=self.LoadClassB)

        anchor_ml.add_widget(btn1)
        anchor_ml.add_widget(btn2)
        self.add_widget(anchor_ml)

    def LoadClassA(self, instance):
        print('Load class A')

    def LoadClassB(self, instance):
        print('Load class B')

class DesignerApp(App):

    def build(self):
        cc = Container()
        return cc


if __name__ == '__main__':
    DesignerApp().run()