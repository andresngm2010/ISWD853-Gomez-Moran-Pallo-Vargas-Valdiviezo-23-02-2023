import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Login Exitoso')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)            
        
        logo =utl.leer_imagen("./imagenes/logo.png", (200, 200))
                        
        label = tk.Label( self.ventana, image=logo,bg='#3a7ff6' )
        label.place(x=0,y=0,relwidth=1, relheight=1)

        labelTexto = tk.Label(text="Login realizado de forma exitosa", background="white")
        labelTexto.place(x=w/2 - 200, y=h-100, relwidth=0.3, relheight=0.05)
        
        self.ventana.mainloop()