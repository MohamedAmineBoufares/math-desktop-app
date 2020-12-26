import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from numpy import sin ,cos,exp,log,sqrt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from sympy import *


class mclass:

    def __init__(self,  window):
        self.window = window
        self.fr1 = Frame(window,highlightbackground="black", highlightthickness=2, width=100, height=100, bd= 5) # à gauche
        self.fr2 = Frame(window,highlightbackground="darkgray", highlightthickness=2, width=100, height=100, bd= 5) # à droite
        self.func_txt=StringVar()
        self.func_txt.set("L'expression de f :")
        self.label_func=Label(self.fr1, textvariable=self.func_txt,justify=RIGHT, height=4)
        self.label_func.grid(row=1,column=0)
        self.a_txt=StringVar()
        self.a_txt.set("a:")
        self.label_a=Label(self.fr1, textvariable=self.a_txt,justify=RIGHT, anchor="w", height=4)
        self.label_a.grid(sticky = E,row=2,column=0)
        self.boxa = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxa.grid(sticky = W,row=2,column=1)
        self.b_txt=StringVar()
        self.b_txt.set("b:")
        self.label_b=Label(self.fr1, textvariable=self.b_txt,justify=RIGHT, anchor="w", height=4)
        self.label_b.grid(sticky = E,row=3,column=0)
        self.boxb = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxb.grid(sticky = W,row=3,column=1)
        self.box = Entry(self.fr1,borderwidth=3,bg="white")
        self.box.grid(row=1,column=1)

        # Dérivé
        self.diriv_txt=StringVar()
        self.diriv_txt.set("Dérivé: ")
        self.label_diriv = Label(self.fr1, textvariable=self.diriv_txt,justify=RIGHT, anchor="w", height=4)
        self.label_diriv.grid(sticky = E, row=5, column=0)
        
        self.res_txt=StringVar()
        self.res_diriv = Label(self.fr1,textvariable=self.res_txt,justify=RIGHT, anchor="w", width=10,borderwidth=3,bg="powder blue")
        self.res_diriv.grid(sticky = W, row=5, column=1)

        # Slider pour le dérivé
        self.s_txt=StringVar()
        self.s_txt.set("Ordre du Dérivé: ")
        self.label_s = Label(self.fr1, textvariable=self.s_txt,justify=RIGHT, anchor="w", height=4)
        self.label_s.grid(sticky = E, row=4, column=0)
        
        self.slider = Scale(self.fr1, from_=1, to=10, orient=HORIZONTAL)
        self.slider.grid(sticky = W, row=4, column=1)

        # Prémitive
        self.pri_txt=StringVar()
        self.pri_txt.set("Primitive: ")
        self.label_pri = Label(self.fr1, textvariable=self.pri_txt,justify=RIGHT, anchor="w")
        self.label_pri.grid(sticky = E, row=6, column=0)
        
        self.resp_txt=StringVar()
        self.res_prim = Label(self.fr1,textvariable=self.resp_txt,justify=RIGHT, anchor="w", width=10,borderwidth=3,bg="powder blue")
        self.res_prim.grid(sticky = W, row=6, column=1)
        
        # Button
        self.button = Button (self.fr1, width =35,text="plot",bg="powder blue", command=self.plot)
        self.button.grid(row=7,column=0,columnspan=3)
        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)
           
        # Figure
        self.fig = Figure(figsize=(6,6))
        self.a = self.fig.add_subplot(111)
        self.a.set_title ("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.set_facecolor("white")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        
        self.x = symbols('x') 
        
    # Plot + Calculation Function
    def plot (self):
        f= lambda x: eval(self.box.get().lower())
        ff= lambda x: self.box.get().lower()
        x=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
        
        pp=np.vectorize(f)
        p= ff(x)

        D = diff(p, self.x, self.slider.get()) # Calcule du Dérivé
        d = lambda x: eval(str(diff(p, self.x, self.slider.get())))
        I = integrate(p, self.x) # Calcule du Primitive
        i = lambda x: eval(str(integrate(p, self.x)))

        d_vect = np.vectorize(d)
        i_vect = np.vectorize(i)

        self.a.cla()
        self.a.set_ylim([float(self.boxa.get()), float(self.boxb.get())])
        self.a.xaxis.set_ticks(np.arange(float(self.boxa.get()), float(self.boxb.get())+1, 1))
        self.a.yaxis.set_ticks(np.arange(float(self.boxa.get()), float(self.boxb.get())+1, 1))
        self.a.set_title ("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.grid(True)
        
        self.a.plot(x, pp(x),color='blue', label='F(X)') # Afficher F(x)
        self.a.plot(x, d_vect(x),color='green', label='Dérivé') # Afficher F'(x)
        self.a.plot(x, i_vect(x),color='red', label="Primitive") # Afficher F-1(x)
        self.a.legend()
        
        
        self.res_txt.set(D) # Afichage du Dérivé dans la GUI
        self.resp_txt.set(I) # Afichage du Primitive dans la GUI
        
        
        print(type(self.slider.get()))
        
        self.canvas.draw()

if __name__ == '__main__':
    
    window= Tk()

    start= mclass(window)

    window.mainloop()





