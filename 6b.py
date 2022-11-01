import tkinter # naimportuje to tkinter
canvas = tkinter.Canvas(width=400, height=400, bg='white') # vytvorí to plátno
canvas.pack() # vykreslí to plátno

canvas.create_oval(20, 270, 80, 330, fill='green') # vykreslí to zelený balón
canvas.create_oval(60, 270, 120, 330, fill='lime') # vykreslí to limetkovo zelený balón ktorý trochu prekrije zelený balón
canvas.create_oval(100, 270, 160, 330, fill='purple') # vykreslí to fialový balón ktorý trochu prekrije limetkovo zelený balón
canvas.create_oval(140, 270, 200, 330, fill='blue') # vykreslí to modrý balón ktorý trochu prekrije fialový balón
canvas.create_oval(180, 270, 240, 330, fill='orange') # vykreslí to oranžový balón ktorý trochu prekrije modrý balón
canvas.create_oval(220, 270, 280, 330, fill='yellow') # vykreslí to žltý balón ktorý trochu prekrije oranžový balón
canvas.create_oval(260, 270, 320, 330, fill='pink') # vykreslí to ružový balón ktorý trochu prekrije žltý balón
canvas.create_oval(300, 270, 360, 330, fill='red') # vykreslí to červený balón ktorý trochu prekrije ružový balón

canvas.create_line(50, 270, 180, 130) # vykreslí to čiaru ktorá ide od stredu zeleného balónu smerom hore
canvas.create_line(90, 270, 180, 130) # vykreslí to čiaru ktorá ide od stredu limetkovo zeleného balónu smerom hore
canvas.create_line(130, 270, 180, 130) # vykreslí to čiaru ktorá ide od stredu fialového balónu smerom hore
canvas.create_line(170, 270, 180, 130) # vykreslí to čiaru ktorá ide od stredu modrého balónu smerom hore
canvas.create_line(210, 270, 180, 130) # vykreslí to čiaru ktorá ide od stredu oranžového balónu smerom hore
canvas.create_line(250, 270, 180, 130) # vykreslí to čiaru ktorá ide od stredu žltého balónu smerom hore
canvas.create_line(290, 270, 180, 130) # vykreslí to čiaru ktorá ide od stredu ružového balónu smerom hore
canvas.create_line(330, 270, 180, 130) # vykreslí to čiaru ktorá ide od stredu červeného balónu smerom hore
