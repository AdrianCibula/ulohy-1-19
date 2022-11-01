import tkinter # naiportuje to tkinter
canvas = tkinter.Canvas(width=400, height=400) # urobí to plátno
canvas.pack() # vykreslí to plátno

canvas.create_line(20, 28, 150, 350) # vykreslí to ľavú tyčku rebríka
canvas.create_line(80, 20, 210, 340) # vykreslí to pravú tyčku rebríka

# vykreslí to schody rebrika od spodu smerom hore
canvas.create_line(140, 340, 213, 330)
canvas.create_line(133, 320, 205, 310)
canvas.create_line(125, 300, 197, 290)
canvas.create_line(118, 280, 190, 270)
canvas.create_line(110, 260, 181, 250)
canvas.create_line(102, 240, 173, 230)
canvas.create_line(94, 220, 165, 210)
canvas.create_line(85, 200, 158, 190)
canvas.create_line(77, 180, 149, 170)
canvas.create_line(69, 160, 142, 150)
canvas.create_line(62, 140, 133, 130)
canvas.create_line(55, 120, 125, 110)
canvas.create_line(46, 100, 118, 90)
canvas.create_line(38, 80, 109, 70)
canvas.create_line(30, 60, 100, 50)
canvas.create_line(22, 40, 94, 30)
