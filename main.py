#!/usr/bin/env python3

import matplotlib.pyplot as plt
from math import pi
import tkinter as tk
from os.path import basename, splitext
import numpy as np



class Application(tk.Tk):

    nazev = basename(splitext(basename(__file__.capitalize()))[0])
    nazev = "Konstruktér grafů"
    


    def quit(self, event = None):
        
        super().quit()

    

    def __init__(self):

        super().__init__(className=self.nazev)

        self.title(self.nazev)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)

        

        #parametry
        self.var_uvod = tk.StringVar()
        self.var_amplituda = tk.IntVar()
        self.var_frekvence = tk.IntVar()
        self.var_periody = tk.IntVar()
        self.var_faz_posun = tk.IntVar()
        

       
        #tabulka
        vcmd = (self.register(self.callback))


        #umisteni
        self.lbl_uvod_grafu = tk.Label(self, text = "Zadejte: ")
        self.lbl_uvod_grafu.grid(row = 1, column = 1, sticky = "w")


        self.lbl_uvod_grafu = tk.Label(self, text = "------------------------------------")
        self.lbl_uvod_grafu.grid(row = 2, column = 1, sticky = "w")
        

        self.lbl_uvod_grafu = tk.Label(self, text = "    Popisek grafu: ")
        self.lbl_uvod_grafu.grid(row = 3, column = 1, sticky = "w")
        self.entry_uvod_grafu = tk.Entry(self, width = 15, textvariable = self.var_uvod)
        self.entry_uvod_grafu.grid(row = 3, column = 2)


        self.lbl_amplituda = tk.Label(self, text = "    Amplitudu: ")
        self.lbl_amplituda.grid(row = 4, column = 1, sticky = "w")
        self.entry_amplituda = tk.Entry(self, width = 15, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_amplituda)
        self.entry_amplituda.grid(row = 4, column = 2)


        self.lbl_frekvence = tk.Label(self, text = "    Frekvenci: ")
        self.lbl_frekvence.grid(row = 5, column = 1, sticky = "w")
        self.entry_frekvence = tk.Entry(self, width = 15, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_frekvence)
        self.entry_frekvence.grid(row = 5, column = 2)
        

        self.lbl_periody = tk.Label(self, text = "    Periodu: ")
        self.lbl_periody.grid(row = 6, column = 1, sticky = "w")
        self.entry_periody = tk.Entry(self, width = 15, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_periody)
        self.entry_periody.grid(row = 6, column = 2)


        self.lbl_faz_posun = tk.Label(self, text = "    Fázový posun: ")
        self.lbl_faz_posun.grid(row = 7, column = 1, sticky = "w")
        self.entry_faz_posun = tk.Entry(self, width = 15, validate="all", validatecommand=(vcmd, '%P'), textvariable = self.var_faz_posun)
        self.entry_faz_posun.grid(row = 7, column = 2)
        

        self.lbl_uvod_grafu = tk.Label(self, text = "------------------------------------")
        self.lbl_uvod_grafu.grid(row = 8, column = 1, sticky = "w")


        self.btn_zobraz = tk.Button(self, text = "Kreslit", command = self.zobraz, width = 15, border = 5, background = "#D4D4D4")
        self.btn_zobraz.grid(row = 9, column = 1)
        

        self.btn_zobraz_example = tk.Button(self, text = "Ze souboru", command = self.nacist, width = 15, border = 5, background = "#D4D4D4")
        self.btn_zobraz_example.grid(row = 9, column = 3)


        #prednastavene hodnoty
        self.var_uvod.set("Přednastavený graf")
        self.var_amplituda.set(20)
        self.var_frekvence.set(8)
        self.var_periody.set(2)
        self.var_faz_posun.set(0)



    def zobraz(self):

        uvod = self.var_uvod.get()
        amplituda = self.var_amplituda.get()
        faz_posun = self.var_faz_posun.get()
        frekvence = self.var_frekvence.get()
        periody = self.var_periody.get()
        
        x = np.linspace(0, periody*1/frekvence, frekvence*10000)
        y = amplituda * (np.sin(2*pi*frekvence*x + np.deg2rad(faz_posun)))

        plt.plot(x, y, label = uvod)
        plt.xlabel
        plt.grid(True)
        plt.legend(loc=3)
        plt.show()



    def nacist(self):
        
        nazev = "soubor-win.txt"
        

        with open(nazev, "r") as f:
            
            radky = []
            x = []
            y = []
            i = 0
            

            while True:
                
                radek = f.readline()
                radky.append(radek.split())
                
                if radek == "":
                    break
                
                x.append(float(radky[i - 1][0]))
                y.append(float(radky[i - 1][1]))
                i = i + 1

        
        plt.plot(x, y, label = nazev)
        plt.xlabel
        plt.grid()
        plt.legend()
        plt.show()



    def callback(self, P):
        
        if str.isdigit(P) or P == "":
            return True
        
        else:
            return False



app = Application()
app.mainloop()

