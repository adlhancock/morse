#! /usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 16:53:13 2017

@author: calvin
"""

import tkinter as tk
#import PIL
import time
from itertools import cycle

ditlength = 0.15 # seconds

class Signal():
    def __init__(self):
        self.morse = ''
        self.plaintext = ''
        self.timelog = ''

class MorseApp(tk.Frame):
    def __init__(self,master=None):
        self.ontime = time.time()
        self.offtime = time.time()
        self.signal = Signal()
        self.morsecharacter=''
        self.morseword=''
        self.plaincharacter=''
        self.plainword=''
                
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
        self.master.title('PyMorse v0.1a')
        #self.colours = cycle(['red','green'])
        
    def createWidgets(self):
        ## define widgets
        self.timestring = tk.StringVar()
        self.plainstring = tk.StringVar()
        self.morsestring = tk.StringVar()
        self.morsebox = tk.Label(self,
                            width=50,
                            height=3,
                            bg='white',
                            textvariable=self.morsestring
                            )
        self.plainbox = tk.Label(self,
                            width=50,
                            height=3,
                            bg='white',
                            textvariable=self.plainstring
                            )
        self.timebox = tk.Label(self,
                            width=20,
                            height=1,
                            #bg='red',
                            textvariable=self.timestring
        self.light = tk.Canvas(self,
                                width=200,
                                height=200,)
        
        self.bulb = self.light.create_oval(10,10,190,190,
                               fill='grey')
        
        self.quitButton = tk.Button(self, 
                                text='Quit\n(Esc)',
                                width=15,
                                height=5,
                                command=self.quit)
        
        self.flashButton = tk.Button(self,
                                     text='Flash\n(Right Ctrl)',
                                     width=15,
                                     height=5)
                                     
        ## assign additional actions to widget events
        self.flashButton.bind("<ButtonPress>",
                              self.lighton)
        self.flashButton.bind("<ButtonRelease>",
                              self.lightoff)
        self.flashButton.bind('<KeyPress-space>',self.lighton)
        self.flashButton.bind('<KeyRelease-space>',self.lightoff)
        self.flashButton.bind('<Escape>',lambda _: self.quit())
        self.quitButton.bind('<Escape>',lambda _: self.quit())
        ## arrange widgets
        self.light.grid(row=0,column=0,columnspan=2)
        self.morsebox.grid(row=1,column=0,columnspan=2)
        self.plainbox.grid(row=2,column=0,columnspan=2)
        self.quitButton.grid(row=3,column=0)        
        self.flashButton.grid(row=3,column=1)
        self.flashButton.focus_force()
                              
    def lighton(self,event):
        """ turn the light on and record times"""
        # start timing while light is on
        self.ontime = time.time()
        # record how long the light was off
        self.timeoff = time.time()-self.offtime
        
        # turn the light on
        self.light.itemconfig(self.bulb,fill='yellow')

        # append the time log
        self.signal.timelog+="{:.2f}\t".format(self.timeoff)
        

    def lightoff(self,event):
        """ turn the light off and record times"""
        # start timing the off period
        self.offtime = time.time()
        # record the duration of the on period
        self.timeon = time.time()-self.ontime

        # interpret the button press as a dit or dah
        if self.timeon > ditlength: symbol='-'
        else: symbol='.'

        # append the current character or start a new character or word
		if self.timeoff > 7*ditlength:  # start a new word
				self.signal.morse+=' '
        elif self.timeoff > 3*ditlength: # start a new character
                self.signal.morse += self.morsecharacter
                #self.plaincharacter = morse_to_plain(self.morsecharacter)
				self.morsecharacter = symbol 
        else: self.character+=symbol # append the current character

        # turn the light off
        self.light.itemconfig(self.bulb,fill='grey')

        # append the time log       
        self.signal.timelog+="{:.2f}\n".format(self.timeon)

        
        # display the flash duration and interpretation
        self.timestring.set('On for: {:5.3f}'.format(self.timeon))
        self.morsestring.set(self.signal.morse)
        self.plainstring.set(self.signal.plaintext)

app = MorseApp()
app.mainloop()
