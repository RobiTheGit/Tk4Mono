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
        global custom        
        global filename
        global entrythingy
        global flags
        global preflags
  
        super().__init__(master)
        try:
            photo = PhotoImage(file = "/usr/local/bin/images/Micon.png")
        except:
            photo = PhotoImage(file = "images/Micon.png")        
        root.iconphoto(False, photo) 
        self.pack()

        leftframe = customtkinter.CTkFrame(
        root
        )        
        leftframe.pack(side = LEFT, fill = BOTH, anchor = NE, padx = 5)
        middleframe = customtkinter.CTkFrame(root)
        middleframe.pack(side = LEFT, fill = BOTH, anchor = NE, padx = 5)
        rightframe = customtkinter.CTkFrame(
        root
        )        
        rightframe.pack(side = LEFT, fill = BOTH, anchor = NE, padx = 5)               
 
        righterframe = customtkinter.CTkFrame(
        root
        )        
        righterframe.pack(side = LEFT, fill = BOTH, anchor = NE, padx = 5)               
	
        inlbl = customtkinter.CTkLabel(
        leftframe, 
        text='Program'
        )
        inlbl.pack() 

        entrythingy = customtkinter.CTkTextbox(leftframe, state='disabled', height = 50)
        entrythingy.pack()

        B2 = customtkinter.CTkButton(leftframe,
        text="Open File",
        command = self.getapp,
        height=30, 
        width=30
        )
        B2.pack()          

        inlbl2 = customtkinter.CTkLabel(
        rightframe, 
        text='Flags/Arguments'
        ) 
        inlbl2.pack() 
        
        inlbl3 = customtkinter.CTkLabel(
        middleframe, 
        text='Mono Options'
        ) 
        inlbl3.pack()                    
        preflags = customtkinter.CTkTextbox(middleframe, state='normal', height = 50)
        preflags.pack()
        inlbl4 = customtkinter.CTkLabel(
        rightframe, 
        text='Program Options'
        ) 
        inlbl4.pack()       
        flags = customtkinter.CTkTextbox(rightframe, state='normal', height = 50)
        flags.pack() 

        B = customtkinter.CTkButton(rightframe,  
        text = 'Run Mono Application',
        command=self.run,
        height=30, 
        width=50
        ) 
        B.pack()

        inlbl3 = customtkinter.CTkLabel(
        righterframe, 
        text='Custom Script (without typing mono)'
        ) 
        inlbl3.pack()            

        custom = customtkinter.CTkTextbox(righterframe, state='normal', height = 50)
        custom.pack() 
                       
        B3 = customtkinter.CTkButton(righterframe,  
        text = 'Run Custom Script',
        command=self.runcustom,
        height=30, 
        width=50
        ) 
        B3.pack()                                        

    def run(self):
        global app
        subprocess.run(f'mono {preflags.get(1.0, END)} "{filename}" {flags.get(1.0, END)}', shell=True)

    def getapp(self):
        global filename
        entrythingy.configure(state='normal')
        entrythingy.delete(1.0, END)
        entrythingy.configure(state='disabled')                
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        entrythingy.configure(state='normal')        
        entrythingy.insert(1.0,filename)
        entrythingy.configure(state='disabled')                

    def runcustom(self):
        global custom
        subprocess.run(f'mono {custom.get(1.0, END)}', shell=True)    

# create the application
title = "Tk4Mono Tk GUI For Mono"
root = customtkinter.CTk(className="Tk4Mono")
root.geometry("850x250")
root.resizable(True,True)
myapp = App(root)
myapp.master.title(title)
myapp.mainloop()
