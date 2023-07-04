from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
from claseImaginario import Imaginario

class Aplicacion():
    __ventana = None
    __n1 = object()
    __n2 = object()
    
    __n1_real=int
    __n1_imag=int
    __n2_real=int
    __n2_imag=int
    
    def __init__(self):
        self.__ventana = Tk()
        #self.__ventana.geometry('500x150')
        self.__ventana.title('Calculadora Números Complejos Imaginarios')
        mainframe = ttk.Frame(self.__ventana, padding='5 12 12 5')
        mainframe.grid(column=0, row=0)
        #mainframe.columnconfigure(0, weight=1)
        #mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        
        self.__n1 = StringVar()
        self.__n2 = StringVar()
        self.__n1_real=StringVar()
        self.__n1_imag=StringVar()
        self.__n2_real=StringVar()
        self. __n2_imag=StringVar()
        self.__rdo = StringVar()
        
        self.n1_realEntry =ttk.Entry(mainframe,textvariable=self.__n1_real, width=10)
        self.n1_realEntry.grid(column=0, row=0)
        ttk.Label(mainframe, text="+").grid(column=1, row=0)
        self.n1_imagEntry=ttk.Entry(mainframe,textvariable=self.__n1_imag, width=10)
        self.n1_imagEntry.grid(column=2, row=0)
        ttk.Label(mainframe, text="i").grid(column=3, row=0)
        
        
        self.n2_realEntry =ttk.Entry(mainframe,textvariable=self.__n2_real, width=10)
        self.n2_realEntry.grid(column=0, row=1)
        ttk.Label(mainframe, text="+").grid(column=1, row=1)
        self.n2_imagEntry =ttk.Entry(mainframe,textvariable=self.__n2_imag, width=10)
        self.n2_imagEntry.grid(column=2, row=1)
        self.__n2 = Imaginario(self.__n2_real, self.__n2_imag)
        ttk.Label(mainframe, text="i").grid(column=3, row=1)
        
        """
        ttk.Button(mainframe, text= '7',command= partial(self.ponerNUMERO, '7')).grid(column=0, row=2, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '8',command= partial(self.ponerNUMERO, '8')).grid(column=1, row=2, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '9',command= partial(self.ponerNUMERO, '9')).grid(column=2, row=2, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '4',command= partial(self.ponerNUMERO, '4')).grid(column=0, row=3, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '5',command= partial(self.ponerNUMERO, '5')).grid(column=1, row=3, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '6',command= partial(self.ponerNUMERO, '6')).grid(column=2, row=3, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '1',command= partial(self.ponerNUMERO, '1')).grid(column=0, row=4, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '2',command= partial(self.ponerNUMERO, '2')).grid(column=1, row=4, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '3',command= partial(self.ponerNUMERO, '3')).grid(column=2, row=4, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '0',command= partial(self.ponerNUMERO, '0')).grid(column=0, row=5, sticky=W, padx=1, pady=1)
        """
        ttk.Button(mainframe, text= '/',command= self.dividir).grid(column=2, row=4,columnspan=2,rowspan=2, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '*',command= self.multiplicar).grid(column=0, row=4,columnspan=2,rowspan=2, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '-',command= self.resta).grid(column=2, row=2,columnspan=2,rowspan=2, sticky=W, padx=1, pady=1)
        ttk.Button(mainframe, text= '+',command= self.suma).grid(column=0, row=2,columnspan=2,rowspan=2, sticky=W, padx=1, pady=1)
        

        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=0, row=7,columnspan=4, sticky="nsew")
        ttk.Label(mainframe, textvariable=self.__rdo,font='Calibri 15').grid(column=1, row=6,columnspan=2, padx=10, pady=10)
        self.__ventana.mainloop()
    def obtenerNro1(self):
        try:
            r = int(self.n1_realEntry.get())
            i = int(self.n1_imagEntry.get())
            return Imaginario(r, i)
        except ValueError:
            messagebox.showerror(title="Error de Valor", message="Debe ingresar números válidos.")
        
    
    def obtenerNro2(self):
        try:
            r = int(self.n2_realEntry.get())
            i = int(self.n2_imagEntry.get())
            return Imaginario(r, i)
        except ValueError:
            messagebox.showerror(title="Error de Valor", message="Debe ingresar números válidos.")
    
    def darRdo(self, rdo):
        if rdo.getImag() < 0:
            self.__rdo.set(str(rdo.getReal()) + "-" + str(abs(rdo.getImag())) + "i")
        else:
            self.__rdo.set(str(rdo.getReal()) + "+" + str(abs(rdo.getImag())) + "i")
        
    def suma (self):
        rdo = self.obtenerNro1() + self.obtenerNro2()
        print (rdo)
        self.darRdo(rdo)
        
        
    def resta(self):
        rdo = self.obtenerNro1() - self.obtenerNro2()
        print (rdo)
        self.darRdo(rdo)
        
    def dividir (self):
        try:
            rdo = self.obtenerNro1() / self.obtenerNro2()
            print (rdo)
            self.darRdo(rdo)
        except ZeroDivisionError:
            messagebox.showerror(title="Error de Division", message="No se puede dividir en 0.")
    
    def multiplicar(self):
        rdo = self.obtenerNro1() * self.obtenerNro2()
        print (rdo)
        self.darRdo(rdo)
        
    def ponerNUMERO(self,valor):
        return 