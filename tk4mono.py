#!/usr/bin/python3 

import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter
import subprocess
from tkinter.filedialog import askopenfilename

class App(tk.Frame):
    def __init__(self, master):
        global app
        global var1
        global filename
        global entrythingy
        global flags
        var1 = tk.IntVar()
        super().__init__(master)
        self.pack()
        
        inlbl = customtkinter.CTkLabel(
        root, 
        text='Program'
        )
        inlbl.pack() 
                
        entrythingy = customtkinter.CTkTextbox(root, state='disabled', height = 50)
        entrythingy.pack()
        
        inlbl2 = customtkinter.CTkLabel(
        root, 
        text='Flags/Arguments'
        ) 
        inlbl2.pack()            
        flags = customtkinter.CTkTextbox(root, state='normal', height = 50)
        flags.pack() 
                       
        B = customtkinter.CTkButton(root,  
        text = 'Run Mono Application',
        command=self.run,
        height=30, 
        width=50
        )                          
        B2 = customtkinter.CTkButton(root,
        text = "Open File",
        command = self.getapp,
        height=30, 
        width=50
        )
        B.pack()
        B2.pack()       
    def run(self):
        global app
        subprocess.run(f'mono "{filename}" {flags.get(1.0, END)}', shell=True)
    def getapp(self):
        global filename
        entrythingy.configure(state='normal')
        entrythingy.delete(1.0, END)
        entrythingy.configure(state='disabled')                
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        entrythingy.configure(state='normal')        
        entrythingy.insert(1.0,filename)
        entrythingy.configure(state='disabled')                
           
# create the application
title = "Tk4Mono Tk GUI For Mono"
root = customtkinter.CTk(className="Tk4Mono")
root.geometry("450x450")
root.resizable(True,True)
myapp = App(root)
myapp.master.title(title)
myapp.mainloop()
