# import kivy
# from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.button import MDRaisedButton
from kivymd.toast import toast
from bresenham import bresenham
import cv2
import numpy as np
import os
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
            ext= ['*.png', '*.jpg', '*.jpeg', '*.bmp']
        )
        self.shape = ''
        self.pic =  ''
        self.pic_path =  ''
    def file_manager_open(self):
        self.file_manager.show('/')  # '/' indicates the start path for the file manager

    def select_path(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        height, width, _ = img.shape
        print(self.shape)
        if self.shape == 'circle' : 
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=200, param2=20, minRadius=0, maxRadius=0)
            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                (x, y, r) = circles[2]
                x_center, y_center = width // 2, height // 2
                x_offset, y_offset = x_center - x, y_center - y
                x, y = x + x_offset, y + y_offset
                cv2.circle(img, (x, y), r, (0, 255, 0), 2)
                    
            img_texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb')
            img_texture.blit_buffer(img.flatten(), colorfmt='rgb', bufferfmt='ubyte')
            self.screen.ids.image.texture = img_texture
            self.screen.ids.image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.screen.ids.save_button.pos_hint = {'center_x': 0.3, 'center_y': 0.1}
            self.screen.ids.close_button.pos_hint = {'center_x': 0.7, 'center_y': 0.1}
            filename = os.path.basename(path)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(os.path.dirname(path), f"{name}_circle{ext}")
            self.pic_path = str(name) + str(ext)
            self.pic = img
            
        if self.shape == 'rectangle' : 
            center_x = img.shape[1] // 2
            center_y = img.shape[0] // 2

            # Calculate la hauteur gauche
            rect_size = 200
            x = center_x - (rect_size // 2)
            y = center_y - (rect_size // 2)

           
            cv2.rectangle(img, (x, y), (x + rect_size, y + rect_size), (0, 255, 0), 2)
            img_texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb')
            img_texture.blit_buffer(img.flatten(), colorfmt='rgb', bufferfmt='ubyte')
            self.screen.ids.image.texture = img_texture
            self.screen.ids.image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.screen.ids.save_button.pos_hint = {'center_x': 0.3, 'center_y': 0.1}
            self.screen.ids.close_button.pos_hint = {'center_x': 0.7, 'center_y': 0.1}
            filename = os.path.basename(path)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(os.path.dirname(path), f"{name}_circle{ext}")
            self.pic_path = str(name) + str(ext)
            self.pic = img
        
        if self.shape == 'triangle' : 
            center = (int(img.shape[1] / 2), int(img.shape[0] / 2))

            # Definit les sommet
            side_length = 300
            v1 = (center[0], center[1] - int(side_length / 2))
            v2 = (center[0] + int(side_length / 2), center[1] + int(side_length / 2))
            v3 = (center[0] - int(side_length / 2), center[1] + int(side_length / 2))
            vertices = np.array([v1, v2, v3])

            # Draw the triangle on the image
            cv2.drawContours(img, [vertices], 0, (0, 255, 0), 2)
            img_texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb')
            img_texture.blit_buffer(img.flatten(), colorfmt='rgb', bufferfmt='ubyte')
            self.screen.ids.image.texture = img_texture
            self.screen.ids.image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.screen.ids.save_button.pos_hint = {'center_x': 0.3, 'center_y': 0.1}
            self.screen.ids.close_button.pos_hint = {'center_x': 0.7, 'center_y': 0.1}
            filename = os.path.basename(path)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(os.path.dirname(path), f"{name}_circle{ext}")
            self.pic_path = str(name) + str(ext)
            self.pic = img
        
        if self.shape == 'ligne' : 
            height, width, channels = img.shape
            x1, y1, x2, y2 = 0, 0, 200, 100
            coords = bresenham(x1, y1, width, height)
            for i in range(len(coords)-1) :
                cv2.line(img, coords[i], coords[i+1], (0, 255, 0), 2)
            img_texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb')
            img_texture.blit_buffer(img.flatten(), colorfmt='rgb', bufferfmt='ubyte')
            self.screen.ids.image.texture = img_texture
            self.screen.ids.image.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.screen.ids.save_button.pos_hint = {'center_x': 0.3, 'center_y': 0.1}
            self.screen.ids.close_button.pos_hint = {'center_x': 0.7, 'center_y': 0.1}
            filename = os.path.basename(path)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(os.path.dirname(path), f"{name}_circle{ext}")
            self.pic_path = str(name) + str(ext)
            self.pic = img
            
            
        self.exit_manager()

    def exit_manager(self, *args):
        self.file_manager.close()
        self.screen.ids.my_label.pos_hint = {'center_x': 0.5, 'center_y': -1}

    def save_image(self):
        random_number1 = np.random.randint(1, 1000)
        random_number2 = np.random.randint(1, 1000)
        cv2.imwrite(str(random_number1) +"_" + str(random_number2)+ "_" +str(self.pic_path)  , cv2.cvtColor(self.pic, cv2.COLOR_RGB2BGR))
        toast("Image saved successfully!")
    
    def stop(self):
        self.screen.ids.image.pos_hint = {'center_x': 0.5, 'center_y': -1}
        self.screen.ids.save_button.pos_hint = {'center_x': 0.3, 'center_y': -1}
        self.screen.ids.close_button.pos_hint = {'center_x': 0.7, 'center_y': -1}
        
    
    def callback(self,instance) : 
        print(instance.icon)
        if instance.icon == 'rectangle' :
            self.shape = 'rectangle'
            self.root.ids.layout.text = ' Dessiner un rectange'
            self.root.ids.my_label.text = 'Charger l\'image'
            self.root.ids.my_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.screen.ids.image.pos_hint = {'center_x': 0.5, 'center_y': -1}
            self.screen.ids.save_button.pos_hint = {'center_x': 0.3, 'center_y': -1}
            self.screen.ids.close_button.pos_hint = {'center_x': 0.7, 'center_y': -1}
            
        elif instance.icon == 'vector-line' :
            self.shape = 'ligne'
            self.root.ids.layout.text = ' Dessiner une ligne'
            self.root.ids.my_label.text = 'Charger l\'image'
            self.root.ids.my_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.screen.ids.image.pos_hint = {'center_x': 0.5, 'center_y': -1}
            self.screen.ids.save_button.pos_hint = {'center_x': 0.3, 'center_y': -1}
            self.screen.ids.close_button.pos_hint = {'center_x': 0.7, 'center_y': -1}
            
        elif instance.icon == 'circle' :
            self.shape = 'circle'
            self.root.ids.layout.text = 'Dessiner un cercle'
            self.root.ids.my_label.text = 'Charger l\'image'
            self.screen.ids.image.pos_hint = {'center_x': 0.5, 'center_y': -1}
            self.root.ids.my_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.screen.ids.save_button.pos_hint = {'center_x': 0.3, 'center_y': -1}
            self.screen.ids.close_button.pos_hint = {'center_x': 0.7, 'center_y': -1}
            
        elif instance.icon == 'triangle' :
            self.shape = 'triangle'
            self.root.ids.layout.text = 'Dessiner un triangle'
            self.root.ids.my_label.text = 'Charger l\'image'
            self.screen.ids.image.pos_hint = {'center_x': 0.5, 'center_y': -1}
            self.root.ids.my_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            self.screen.ids.save_button.pos_hint = {'center_x': 0.3, 'center_y': -1}
            self.screen.ids.close_button.pos_hint = {'center_x': 0.7, 'center_y': -1}
    
    def build(self):
       
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette ="BlueGray"  
        self.screen = Builder.load_file('amd.kv')
        return self.screen

    

if __name__ == "__main__":
    AmdApp().run()