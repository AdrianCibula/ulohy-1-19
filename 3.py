import tkinter # naimportuje to tkinter
canvas = tkinter.Canvas(width=400, height=400, bg='white') # vytvorí to plátno
canvas.pack() # vykreslí to plátno

canvas.create_oval(140, 70, 210, 140, fill='blue') # vykreslí to modrý balón
canvas.create_line(150, 129, 170, 210, width=2) # vykreslí to ľavú čiaru od balónu dole
canvas.create_line(197, 130, 170, 210, width=2) # vykreslí to pravú čiaru do balónu dole
canvas.create_rectangle(150, 210, 197, 225, fill='red', width=2) # vykreslí to červený obdĺžnik ktorý je napojený na čiary



