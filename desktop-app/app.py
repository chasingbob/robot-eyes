import datetime
from math import sin

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
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.garden.graph import Graph, MeshLinePlot



Builder.load_file('app.kv')

class GraphWidget(Widget):
    def update(self, *args):
        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)

class MainTab(TabbedPanel):
    def __init__(self, **kwargs):
        super(MainTab, self).__init__(**kwargs)
    
        tab1 = TabbedPanelHeader(text='Compile')
        tab1.content = Label(text='test')

        self.add_widget(tab1)

class TabbedPanelApp(App):
    def build(self):
        return MainTab()



if __name__ == '__main__':
    TabbedPanelApp().run()