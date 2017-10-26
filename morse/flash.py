# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:53:13 2017

@author: calvin
"""

import tkinter as tk
import PIL
from time import sleep as wait

root1 = tk.Tk()
root1.wm_title('Morse')

#label = tk.Label(root1, text="Morse")
#label.pack(side=tk.TOP)

flasher = tk.Canvas(root1, width=200,height=200)
flasher.pack()
rect = flasher.create_rectangle(10,10,190,190,fill='grey')
x = input('go')
flasher.itemconfig(rect,fill='red')
x = input('stop')
flasher.itemconfig(rect,fill='grey')


#root1.mainloop()