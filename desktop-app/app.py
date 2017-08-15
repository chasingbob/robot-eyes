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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.core.window import Window

import matplotlib.pyplot as plt

Builder.load_file('app.kv')


class MainTab(TabbedPanel):
    pass

class TabbedPanelApp(App):
    def build(self):
        return MainTab()



if __name__ == '__main__':
    TabbedPanelApp().run()