import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import numpy as np
from numpy import *
from sympy import *
from scipy.integrate import quad 
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showwarning

class RectangleG ( object ) :
    def __init__ (self , a , b , n , f ) :
        self.a = a
        self.b = b
        self.x = np.linspace( a , b , n+1 )
        self.f = f
        self.n = n
    def integrate ( self , f ) :
        x= self.x
        y= f( x )
        h = float( x[1] - x[0] )
        s = sum( y[ 0 : -1 ] )
        return h * s
    def Graph ( self , f , resolution =1001 ) :
        xl = self.x
        yl = f(xl)
        xlist_fine =np.linspace( self.a , self.b , resolution )
        for i in range ( self.n ) :
            x_rect = [xl[ i ] , xl[ i ] , xl[ i + 1 ] , xl[i+1] , xl[ i ] ] # abscisses des sommets
            y_rect = [0 , yl[ i ] , yl[ i ] , 0 , 0 ] # ordonnees des sommets
            plt.plot ( x_rect , y_rect , 'r' )
        yflist_fine = f ( xlist_fine )
        plt.plot ( xlist_fine , yflist_fine )
        plt.plot(xl, yl,"bo")
        plt.xlabel ( 'x' )
        plt.ylabel ( ' f ( x ) ' )
        plt.title('Methode des Rectangles Gauches, N = {}'.format(self.n))
     
class Milieu(object):
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        h = float(self.b-self.a)/self.n
        result = 0
        for i in range(self.n):
            result += f((self.a + h/2.0) + i*h)
        result *= h
        return result
    def Graph ( self , f , resolution =1001 ) :
        xl = self.x
        yl = f(xl)
        xlist_fine =np.linspace( self.a , self.b , resolution )
        for i in range ( self.n ) :
            mi = (xl[i]+xl[i+1])/2
            x_rect = [xl[ i ] , xl[ i ],xl[ i+1 ],xl[ i+1 ],xl[ i ]] # abscisses des sommets
            y_rect = [0 , f(mi),f(mi),0,0] # ordonnees des sommets
            plt.plot(x_rect,y_rect,'r')
            plt.plot ( mi , f(mi) , 'bo' )
        yflist_fine = f ( xlist_fine )
        plt.plot ( xlist_fine , yflist_fine )
        plt.xlabel ( 'x' )
        plt.ylabel ( ' f ( x ) ' )
        plt.title('Methode de Point Milieu, N = {}'.format(self.n))

class Trapezoidal(object):
    def __init__(self, a, b, n, f):
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)
        self.f = f
        self.n = n
    def integrate(self,f):
        x=self.x
        y=f(x)
        h = float(x[1] - x[0])
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0
    def Graph(self,f,resolution=1001):
        xl = self.x
        yl = f(xl)
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
            y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] # ordonnees des sommets
            plt.plot(x_rect, y_rect,"r")
        yflist_fine = f(xlist_fine)
        plt.plot(xlist_fine, yflist_fine)#plot de f(x)
        plt.plot(xl, yl,"cs")#point support
        plt.ylabel ( ' f ( x ) ' )
        plt.title('Methode des Trapézes, N = {}'.format(self.n))

class Simps(object):
    def __init__(self, a, b, n, f): #initialiser les paramètres du classe
        self.a = a
        self.b = b
        self.x = np.linspace(a, b, n+1)#les pts supports
        self.f = f
        self.n = n #nombre de subdivision

    def integrate(self,f):#calculer la somme ((b-a)/6*n)*[f(a)+2*sum(xi)+4*sum(mi)+f(b)]
        x=self.x #les points supports xi #x(0)=a-->x(n)=b
        y=f(x) #yi variable local y(o)=f(xo)-->y(n)
        h = float(x[1] - x[0])#pas h=(b-a)/2*n
        n = len(x) - 1#nombre subdivision
        if n % 2 == 1:#si le reste de la division =1 impaire
            n -= 1
        s = y[0] + y[n] + 4.0 * sum(y[1:-1:2]) + 2.0 * sum(y[2:-2:2])
        return h * s / 3.0
    def Graph(self,f,resolution=1001):
        xl = self.x 
        yl = f(xl) 
        xlist_fine=np.linspace(self.a, self.b, resolution)
        for i in range(self.n):
            xx=np.linspace(xl[i], xl[i+1], resolution)
            m=(xl[i]+xl[i+1])/2#pt milieu
            aa=xl[i]#borne gauche
            bb=xl[i+1]#borne droite
            l0 = (xx-m)/(aa-m)*(xx-bb)/(aa-bb)
            l1 = (xx-aa)/(m-aa)*(xx-bb)/(m-bb)
            l2 = (xx-aa)/(bb-aa)*(xx-m)/(bb-m)
            P = f(aa)*l0 + f(m)*l1 + f(bb)*l2#
            plt.plot(xx,P,'r')
            plt.plot(m,f(m),"r",marker="s")
        yflist_fine = f(xlist_fine)#fontion f
        plt.plot(xlist_fine, yflist_fine,'b')
        plt.plot(xl, yl,'bo')#point support en bleu rond
        plt.ylabel('f(x)')
        plt.title('Methode de Simpson, N = {}'.format(self.n))

class mclass:

    def __init__(self,  window):
        
        self.window = window
        self.window.title("Projet Analyse Numérique")
        self.window.geometry("1366x768")
        self.fr1 = Frame(window,highlightbackground="DarkOrange1", highlightthickness=2, width=100, height=200, bd= 5) # Frame à gauche
        self.fr2 = Frame(window,highlightbackground="black", highlightthickness=2, width=100, height=200, bd= 5) # Frame au milieu
        self.fr3 = Frame(window,highlightbackground="brown1", highlightthickness=2, width=200, height=300, bd= 5) # Frame à droite
        self.func_txt=StringVar()
        self.func_txt.set("L'expression de f :")
        self.label_func=Label(self.fr1, textvariable=self.func_txt,justify=RIGHT, height=4, font=("Arial", 12))
        self.label_func.grid(row=1,column=0)
        
        self.a_txt=StringVar()
        self.a_txt.set("A:")
        self.label_a=Label(self.fr1, textvariable=self.a_txt,justify=RIGHT, anchor="w", height=4, font=("Arial", 12))
        self.label_a.grid(sticky = E,row=2,column=0)
        self.boxa = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxa.grid(sticky = W,row=2,column=1)
        self.b_txt=StringVar()
        self.b_txt.set("B:")
        self.label_b=Label(self.fr1, textvariable=self.b_txt,justify=RIGHT, anchor="w", height=4, font=("Arial", 12))
        self.label_b.grid(sticky = E,row=3,column=0)
        self.boxb = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxb.grid(sticky = W,row=3,column=1)
        self.box = Entry(self.fr1,borderwidth=3,bg="white")
        self.box.grid(row=1,column=1)
       
        # Dérivé
        self.diriv_txt=StringVar()
        self.diriv_txt.set("Dérivé: ")
        self.label_diriv = Label(self.fr1, textvariable=self.diriv_txt,justify=RIGHT, anchor="w", height=4, font=("Arial", 12))
        self.label_diriv.grid(sticky = E, row=5, column=0)
        
        self.res_txt=StringVar()
        self.res_diriv = Label(self.fr1,textvariable=self.res_txt,justify=RIGHT, anchor="w", width=10,borderwidth=3,bg="powder blue")
        self.res_diriv.grid(sticky = W, row=5, column=1)

        # Slider pour le dérivé
        self.s_txt=StringVar()
        self.s_txt.set("Ordre du Dérivé: ")
        self.label_s = Label(self.fr1, textvariable=self.s_txt,justify=RIGHT, anchor="w", height=4, font=("Arial", 12))
        self.label_s.grid(sticky = E, row=4, column=0)
        
        self.slider = Scale(self.fr1, from_=1, to=5, orient=HORIZONTAL)
        self.slider.grid(sticky = W, row=4, column=1)

        # Prémitive
        self.pri_txt=StringVar()
        self.pri_txt.set("Primitive: ")
        self.label_pri = Label(self.fr1, textvariable=self.pri_txt,justify=RIGHT, anchor="w", font=("Arial", 12))
        self.label_pri.grid(sticky = E, row=6, column=0)
        
        self.resp_txt=StringVar()
        self.res_prim = Label(self.fr1,textvariable=self.resp_txt,justify=RIGHT, anchor="w", width=10,borderwidth=3,bg="powder blue")
        self.res_prim.grid(sticky = W, row=6, column=1)

        # Check_Buttons

            # Afficher (ou pas) F(x)
        self.chbf_txt=StringVar()
        self.chbf_txt.set("Afficher F(x) ")
        self.label_chbf = Label(self.fr1, textvariable=self.chbf_txt,justify=RIGHT, anchor="w", font=("Arial", 12))
        self.label_chbf.grid(sticky = E, row=7, column=0)
        
        self.chbf=BooleanVar() 
        self.res_chbf = Checkbutton(self.fr1,var=self.chbf,justify=RIGHT, anchor="w", width=10,borderwidth=3, command = self.afficher_F,
                                                                                                                    activebackground="blue")
        self.res_chbf.grid(sticky = W, row=7, column=1)

            # Afficher (ou pas) le dérivé
        self.chbd_txt=StringVar()
        self.chbd_txt.set("Afficher le dérivé ")
        self.label_chbd = Label(self.fr1, textvariable=self.chbd_txt,justify=RIGHT, anchor="w", font=("Arial", 12))
        self.label_chbd.grid(sticky = E, row=8, column=0)
        
        self.chbd=BooleanVar() 
        self.chbd.set(False)
        self.res_chbd = Checkbutton(self.fr1, var=self.chbd,justify=RIGHT, anchor="w", width=10,borderwidth=3, command = self.afficher_D,
                                                                                                                    activebackground="green")
        self.res_chbd.grid(sticky = W, row=8, column=1)

            # Afficher (ou pas) le primitive
        self.chbp_txt=StringVar()
        self.chbp_txt.set("Afficher le prémitive ")
        self.label_chbp = Label(self.fr1, textvariable=self.chbp_txt,justify=RIGHT, anchor="w", font=("Arial", 12))
        self.label_chbp.grid(sticky = E, row=9, column=0)
        
        self.chbp=BooleanVar() 
        self.res_chbp = Checkbutton(self.fr1, var=self.chbp,justify=RIGHT, anchor="w", width=10,borderwidth=3, command = self.afficher_P,
                                                                                                                    activebackground="red")
        self.res_chbp.grid(sticky = W, row=9, column=1)

        # Button
        self.button = Button (self.fr1, width =15,text="Afficher",bg="powder blue", command=self.plot, font=("Arial", 12))
        self.button.grid(row=10,column=0,columnspan=3)
        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)

        # Partie pour le calcule d'intégrale

            # Label
        self.integ_txt=StringVar()
        self.integ_txt.set("Si tu veux calculer la V.A de l'intégrale: ")
        self.label_integ = Label(self.fr3, textvariable=self.integ_txt,justify=RIGHT, anchor="w", height=4, font=("Arial", 12))
        self.label_integ.grid(row=1,column=0,columnspan=3)

            # ComboBox
        self.meth_txt=StringVar()
        self.meth_txt.set("Choisir une méthode: ")
        self.label_meth = Label(self.fr3, textvariable=self.meth_txt,justify=RIGHT, anchor="w",height=4, font=("Arial", 12))
        self.label_meth.grid(sticky = E, row=2, column=0)
        
        self.meth = Combobox(self.fr3,values=["---","Rectangle", "Trapéze", "Simpson", "Point Milieu"], state="readonly")
        self.meth.current(0)                                                                                                        
        self.meth.grid(sticky = W, row=2, column=1)
        
            # Borne Inf :
        self.integ_txt=StringVar()
        self.integ_txt.set("Donner borne inf: ")
        self.label_integ = Label(self.fr3, textvariable=self.integ_txt,justify=RIGHT, anchor="w",height=4, font=("Arial", 12))
        self.label_integ.grid(sticky = E,row=3,column=0)
    
        self.boxinf = Entry(self.fr3,width=10,borderwidth=3,bg="yellow green")
        self.boxinf.grid(sticky = W,row=3,column=1)

            # Borne Sup :
        self.integ_txt_2=StringVar()
        self.integ_txt_2.set("Donner borne sup: ")
        self.label_integ_2 = Label(self.fr3, textvariable=self.integ_txt_2,justify=RIGHT, anchor="w",height=4, font=("Arial", 12))
        self.label_integ_2.grid(sticky = E,row=4,column=0)
    
        self.boxsup = Entry(self.fr3,width=10,borderwidth=3,bg="yellow green")
        self.boxsup.grid(sticky = W,row=4,column=1)

            # Slider pour nombre de divison
        self.n_txt=StringVar()
        self.n_txt.set("Nombre de divison: ")
        self.label_n = Label(self.fr3, textvariable=self.n_txt,justify=RIGHT, anchor="w", height=4, font=("Arial", 12))
        self.label_n.grid(sticky = E, row=5, column=0)
        
        self.slider_n = Scale(self.fr3, from_=1, to=10, orient=HORIZONTAL)
        self.slider_n.grid(sticky = W, row=5, column=1)

            # Labels des reusltats
                # Valeur Exacte = V.E
        self.ve_txt=StringVar()
        self.ve_txt.set("Valeur Exacte: ")
        self.label_ve = Label(self.fr3, textvariable=self.ve_txt,justify=RIGHT, anchor="w", height=4, font=("Arial", 12))
        self.label_ve.grid(sticky = E, row=6, column=0)
        
        self.res_ve_txt=StringVar()
        self.res_ve = Label(self.fr3,textvariable=self.res_ve_txt,justify=RIGHT, anchor="w", width=10,borderwidth=3,bg="yellow green")
        self.res_ve.grid(sticky = W, row=6, column=1)

                # Valeur Approché = V.A
        self.va_txt=StringVar()
        self.va_txt.set("Valeur Approché: ")
        self.label_va = Label(self.fr3, textvariable=self.va_txt,justify=RIGHT, anchor="w", height=4, font=("Arial", 12))
        self.label_va.grid(sticky = E, row=7, column=0)
        
        self.res_va_txt=StringVar()
        self.res_va = Label(self.fr3,textvariable=self.res_va_txt,justify=RIGHT, anchor="w", width=10,borderwidth=3,bg="yellow green")
        self.res_va.grid(sticky = W, row=7, column=1)

                # Erreur
        self.er_txt=StringVar()
        self.er_txt.set("Erreur: ")
        self.label_er = Label(self.fr3, textvariable=self.er_txt,justify=RIGHT, anchor="w", height=4, font=("Arial", 12))
        self.label_er.grid(sticky = E, row=8, column=0)
        
        self.res_e_txt=StringVar()
        self.res_e = Label(self.fr3,textvariable=self.res_e_txt,justify=RIGHT, anchor="w", width=10,borderwidth=3,bg="yellow green")
        self.res_e.grid(sticky = W, row=8, column=1)
        

            # Button
        self.button_2 = Button (self.fr3, width =15,text="Afficher",bg="yellow green", command=self.choice, font=("Arial", 12))
        self.button_2.grid(row=9,column=0,columnspan=3)
        self.fr3.grid(row=1,column=2,padx=10,pady=10)
       
        # Figure
        self.fig = Figure(figsize=(6,6))
        self.a = self.fig.add_subplot(111)
        self.a.set_title ("Graphe de f", fontsize=16)
        self.a.set_ylabel("y", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.set_facecolor("white")
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()
        self.x = symbols('x')
           
    # Plot + Calculation Function

    def plot (self):
        
        self.chbf.set(False)
        self.chbd.set(False)
        self.chbp.set(False)

        f= lambda x: eval(self.box.get().lower())
        ff= lambda x: self.box.get().lower()
        self.t=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
        
        self.pp=np.vectorize(f)
        p= ff(self.t)

        D = diff(p, self.x, self.slider.get()) # Calcule du Dérivé
        d = lambda x: eval(str(diff(p, self.x, self.slider.get())))
        I = integrate(p, self.x) # Calcule du Primitive
        i = lambda x: eval(str(integrate(p, self.x)))

        self.d_vect = np.vectorize(d)
        self.i_vect = np.vectorize(i)

        self.a.cla()
        self.a.set_ylim([float(self.boxa.get()), float(self.boxb.get())])
        self.a.xaxis.set_ticks(np.arange(float(self.boxa.get()), float(self.boxb.get())+1, 1))
        self.a.yaxis.set_ticks(np.arange(float(self.boxa.get()), float(self.boxb.get())+1, 1))
        self.a.set_title ("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.grid(True)
    
        self.res_txt.set(D) # Afichage du Dérivé dans la GUI
        self.resp_txt.set(I) # Afichage du Primitive dans la GUI
        self.canvas.draw()

    def afficher_F(self):

            if self.chbf.get():
                self.a.plot(self.t, self.pp(self.t),color='blue', label='F(X)') # Afficher F'(x)
                handles, self.labels = self.a.get_legend_handles_labels()
                self.a.legend()
                self.canvas.draw()

            else:  
                handles, self.labels = self.a.get_legend_handles_labels()
                j=-1

                for i in self.labels :

                    j+=1

                    if i == "F(X)" :

                        del self.a.lines[j] # Supprimer F(x)
                        self.a.legend()
                        self.canvas.draw()

    def afficher_D(self):
            
            if self.chbd.get():
                
                self.a.plot(self.t, self.d_vect(self.t),color='green', label='Dérivé') # Afficher F'(x)
                handles, self.labels = self.a.get_legend_handles_labels()
                self.a.legend()
                self.canvas.draw()

            else :
                handles, self.labels = self.a.get_legend_handles_labels()
                j=-1

                for i in self.labels :

                    j+=1

                    if i == "Dérivé" :

                        del self.a.lines[j] # Supprimer F'(x)
                        self.a.legend()
                        self.canvas.draw()
              
    def afficher_P(self):
            
            if self.chbp.get():

                self.a.plot(self.t, self.i_vect(self.t),color='red', label="Primitive") # Afficher F-1(x)
                handles, self.labels = self.a.get_legend_handles_labels()
                self.a.legend()
                self.canvas.draw()

            else :
                handles, self.labels = self.a.get_legend_handles_labels()
                j=-1

                for i in self.labels :

                    j+=1

                    if i == "Primitive" :

                        del self.a.lines[j] # Supprimer F'(x)
                        self.a.legend()
                        self.canvas.draw()
                
    
    def affichier_Rect(self):

        a = int(self.boxinf.get())
        b = int(self.boxsup.get())
        n = self.slider_n.get()
        x = np.linspace(a, b, n+1)
        
        f= lambda x: eval(self.box.get().lower())
        fx=np.vectorize(f)
        
        R = RectangleG(a, b, n, fx)

        fig = plt.figure()
        
        ax = fig.add_subplot(111)

        I,r = quad(fx, a, b)
        R.Graph(fx)

        self.res_ve_txt.set("%12.4f"%I)
        self.res_va_txt.set("%12.4f"% (R.integrate(fx)))
        self.res_e_txt.set("%12.4f"% (I-R.integrate(fx)))
        
        plt.grid(True)
        plt.show()

    def afficher_Milieu(self):

        a = int(self.boxinf.get())
        b = int(self.boxsup.get())
        n = self.slider_n.get()
        x = np.linspace(a, b, n+1)

        f= lambda x: eval(self.box.get().lower())
        fx=np.vectorize(f)
        
        M = Milieu(a,b,n,fx)

        fig = plt.figure()
        
        ax = fig.add_subplot(111)
       
        I,r = quad(fx, a, b)
        M.Graph(fx)

        self.res_ve_txt.set("%12.4f"%I)
        self.res_va_txt.set("%12.4f"% (M.integrate(fx)))
        self.res_e_txt.set("%12.4f"% (I-M.integrate(fx)))
        
        plt.grid(True)
        plt.show()

    def afficher_Trapez(self):

        a = int(self.boxinf.get())
        b = int(self.boxsup.get())
        n = self.slider_n.get()
        x = np.linspace(a, b, n+1)

        f= lambda x: eval(self.box.get().lower())
        fx=np.vectorize(f)
        
        T = Trapezoidal(a, b, n, fx)

        fig = plt.figure()
        
        ax = fig.add_subplot(111)
        I,r = quad(fx, a, b)
        T.Graph(fx)
    
        self.res_ve_txt.set("%12.4f"%(I))
        self.res_va_txt.set("%12.4f"% (T.integrate(fx)))
        self.res_e_txt.set("%12.4f"% (I-T.integrate(fx)))

        plt.grid(True)
        plt.show()

    def afficher_Simpson(self):

        a = int(self.boxinf.get())
        b = int(self.boxsup.get())
        n = self.slider_n.get()
        x = np.linspace(a, b, n+1)

        f= lambda x: eval(self.box.get().lower())
        fx=np.vectorize(f)
        
        S = Simps(a, b, n, fx)

        fig = plt.figure()
        
        ax = fig.add_subplot(111)
        I,r = quad(fx, a, b)
        S.Graph(fx)

        self.res_ve_txt.set("%12.4f"%(I))
        self.res_va_txt.set("%12.4f"% (S.integrate(fx)))
        self.res_e_txt.set("%12.4f"% (I-S.integrate(fx)))

        plt.grid(True)
        plt.show()

    def choice(self):
        ch = self.meth.get()
        
        if ch == "Rectangle":
            self.affichier_Rect()
        
        elif ch == "Point Milieu":
            self.afficher_Milieu()
        
        elif ch == "Trapéze":
            self.afficher_Trapez()
        
        elif ch == "Simpson":
            self.afficher_Simpson()

        else:
            showwarning("Warning", "Vous avez oubliez un paramétre \nou bien vous n'aves pas selectioner une méthode")

if __name__ == '__main__':
    
    window= Tk()

    start= mclass(window)

    window.mainloop()