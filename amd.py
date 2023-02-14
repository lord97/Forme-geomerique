# import kivy
# from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.widget import Widget
# from kivy.uix.image import Image
# import cv2
# import numpy as np

# class Amd(Widget):
#     pass 

class AmdApp(MDApp):
    
    #dans ce dictionnaire la clé est nom du menu, et la valeur est le nom de l'icone material qui se trouve sur  https://pictogrammers.com/library/mdi/
    data = {
        "Rectangle" : "rectangle",
        "Droite" : "vector-line",
        "Cercle" : "circle",
        "Triangle" : "triangle"
        
    } 
    
    def callback(self,instance) : 
        if instance.icon == 'rectangle' :
            self.root.ids.my_label.text = ' on doit dessiner un rectange'
        elif instance.icon == 'vertor-line' :
            self.root.ids.my_label.text = ' on doit dessiner une ligne'
        elif instance.icon == 'circle' :
            self.root.ids.my_label.text = ' on doit dessiner un cercle'
        elif instance.icon == 'triangle' :
            self.root.ids.my_label.text = ' on doit dessiner un triangle'
    
    def build(self):
       
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette ="BlueGray"  
        return Builder.load_file('amd.kv')

    

if __name__ == "__main__":
    AmdApp().run()