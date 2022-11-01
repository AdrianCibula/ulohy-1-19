import tkinter # naimportuje to tkinter
from random import * # naiportuje to všetko z knižnice random
canvas = tkinter.Canvas(width=400, heigh=400) # vytvorí to plátno
canvas.pack() # vykreslí to plátno

x=100 # nastaví to premennú x na hodnotu 100
y=100 # nastaví to premennú y na hodnotu 100

def kod(x, y): # funkcia kod
    canvas.create_line(x, 0, 410, y, fill='blue') # urobí to modru čiaru

for i in range(1,45): # 44 krát to zopakuje prikaz ktorý je pod ním
    kod(i*10, 415) # vykreslí to funkciu kod 
