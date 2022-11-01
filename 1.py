import tkinter # naimportuje to plátno
canvas = tkinter.Canvas(width=400, heigh=400, bg='white') # vytvorí to plátno
canvas.pack() # vykreslí to plátno

canvas.create_line(120, 120, 240, 120, 180, 250, 120, 120) # vytvorí to čary do tvaru trojuholnika (kornútok)

canvas.create_oval(145, 20, 213, 80, fill='red') # vytvorí to červený kopček
canvas.create_oval(120, 50, 190, 120, fill='yellow') # vytvori to žltý kopček ktorý prekrije ten červený
canvas.create_oval(170, 50, 240, 120, fill='green') # vytvori to zelený kopček ktorý prekrije červený a žltý
canvas.create_rectangle(120, 100, 240, 120, fill='white') # vytvorí to obdĺžnik nad trojuholnikom
