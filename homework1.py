from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class FirstScreen(Screen):
  def __init__(self, name ='First'):
    super().__init__(name=name)
    txt = Label(text = "Перший Екран", color = "red")
    btn1 = Button(text='Back')
    btn1.on_press = self.back

    layout = BoxLayout(orientation = 'vertical', padding = 6, spacing = 4)
    layout.add_widget(txt)
    layout.add_widget(btn1)

    self.add_widget(layout)

  def back(self):
    self.manager.transition.direction = 'right'
    self.manager.current = 'Main'

class SecondScreen(Screen):
  def __init__(self, name ='Second'):
    super().__init__(name=name)
    txt = Label(text = "Другий Екран", color = "orange")
    btn1 = Button(text='Back')
    btn1.on_press = self.back

    layout = BoxLayout(orientation = 'vertical', padding = 6, spacing = 4)
    layout.add_widget(txt)
    layout.add_widget(btn1)

    self.add_widget(layout)

  def back(self):
    self.manager.transition.direction = 'right'
    self.manager.current = 'Main'

class ThirdScreen(Screen):
  def __init__(self, name ='Second'):
    super().__init__(name=name)
    txt = Label(text = "Третій Екран", color = "blue")
    btn1 = Button(text='Back')
    btn1.on_press = self.back

    layout = BoxLayout(orientation = 'vertical', padding = 6, spacing = 4)
    layout.add_widget(txt)
    layout.add_widget(btn1)

    self.add_widget(layout)

  def back(self):
    self.manager.transition.direction = 'right'
    self.manager.current = 'Main'

class FourthScreen(Screen):
  def __init__(self, name ='Second'):
    super().__init__(name=name)
    txt = Label(text = "Четвертий Екран", color = "pink")
    btn1 = Button(text='Back')
    btn1.on_press = self.back

    layout = BoxLayout(orientation = 'vertical', padding = 6, spacing = 4)
    layout.add_widget(txt)
    layout.add_widget(btn1)

    self.add_widget(layout)

  def back(self):
    self.manager.transition.direction = 'right'
    self.manager.current = 'Main'

class ScrButton(Screen):
  def __init__(self, name ='Main', manager=None):
    super().__init__(name=name)
    txt = Label(text = "Вибери екран", color = "yellow")
    btn1 = Button(text='1', color = "red", bold = True)
    btn2 = Button(text='2', color = "orange", bold = True)
    btn3 = Button(text='3', color = "blue", bold = True)
    btn4 = Button(text='4', color = "pink", bold = True)
    btn1.on_press = self.pressed1
    btn2.on_press = self.pressed2
    btn3.on_press = self.pressed3
    btn4.on_press = self.pressed4

    layout = BoxLayout()
    layout1 = BoxLayout(orientation = 'vertical', padding = 6, spacing = 4)
    layout.add_widget(txt)
    layout1.add_widget(btn1)
    layout1.add_widget(btn2)
    layout1.add_widget(btn3)
    layout1.add_widget(btn4)
    layout.add_widget(layout1)

    self.add_widget(layout)

  def pressed1(self):
    self.manager.transition.direction = 'left'
    self.manager.current = 'First'

  def pressed2(self):
    self.manager.transition.direction = 'left'
    self.manager.current = 'Second'

  def pressed3(self):
    self.manager.transition.direction = 'left'
    self.manager.current = 'Third'

  def pressed4(self):
    self.manager.transition.direction = 'left'
    self.manager.current = 'Fourth'

class MyApp(App):
  def build(self):
    sm = ScreenManager()
    sm.add_widget(ScrButton(name='Main', manager=sm)) 
    sm.add_widget(FirstScreen(name='First'))
    sm.add_widget(SecondScreen(name='Second'))
    sm.add_widget(ThirdScreen(name='Third'))
    sm.add_widget(FourthScreen(name='Fourth'))
    return sm

MyApp().run()


































# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout

# class FirstScreen(Screen):
#     def __init__(self, name ='First'):
#         super().__init__(name=name)
#         btn2 = Button(text='Back')
#         self.add_widget(btn2)

# class ScrButton(Screen):
#     def __init__(self, name ='Main'):
#         super().__init__(name=name)
#         btn1 = Button(text='1')
#         btn1.on_press = self.pressed1
#         layout = BoxLayout()
#         layout.add_widget(btn1)

#         return layout


#     def pressed1(self):
#         self.manager.current = 'First'

# class MyApp(App):
#     def build(self):
#         sm = ScreenManager()
#         sm.add_widget(ScrButton)
#         return sm

# MyApp().run()

