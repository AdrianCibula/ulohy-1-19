import tkinter # naimportuje to tkinter
canvas = tkinter.Canvas(width=400, height=400) # vytvorí to plátno
canvas.pack() # vykreslí to plátno

canvas.create_rectangle(160, 150, 190, 240, fill='black') # vykreslí to čierny obdĺžnik
canvas.create_oval(130, 70, 220, 160, fill='green') # vylreslí to zelený oval ktorý trochu prekrije obdĺžnik

# vykreslí to stonky na strome
canvas.create_line(190, 110, 180, 125, width=2)
canvas.create_line(190, 110, 200, 125, width=2)

# vykreslí to čerešne
canvas.create_oval(175, 125, 185, 135, fill='red')
canvas.create_oval(195, 125, 205, 135, fill='red')
