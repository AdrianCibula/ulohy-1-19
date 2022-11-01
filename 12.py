import tkinter # naimportuje to tkinter
canvas = tkinter.Canvas(width=400, height=400) # urobí to plátno
canvas.pack() # vykreslí to plátno

maxx = int(canvas["width"]) # nastaví to premennú maxx na čislo ktoré je v 2 riadku width
maxy = int(canvas["height"]) # nastaví to premennú maxy na čislo ktoré je v 2 riadku height

for i in range(0, maxx, 10): # urobí to príkaz pod tým nejaký počet krát
    canvas.create_line(i, 0, i, maxy, fill='black') # urobí to horizontálne čiary

for i in range(0, maxy, 10): # urobí to príkaz pod tým nejaký počet krát
    canvas.create_line(0, i, maxx, i, fill='black') # urobí to vertikálne čiary
