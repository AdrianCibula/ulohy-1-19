import tkinter # naimportuje to tkinter
canvas = tkinter.Canvas(width=400, height=400, bg='white') # vytvorí to plátno
canvas.pack() # vykreslí to plátno

canvas.create_oval(20, 90, 80, 150, fill='green') # vykreslí to zelený balón
canvas.create_oval(60, 90, 120, 150, fill='lime') # vykreslí to limetkovo zelený balón ktorý trochu prekrije zelený balón
canvas.create_oval(100, 90, 160, 150, fill='purple') # vykreslí to fialový balón ktorý trochu prekrije limetkovo zelený balón
canvas.create_oval(140, 90, 200, 150, fill='blue') # vykreslí to modrý balón ktorý trochu prekrije fialový balón
canvas.create_oval(180, 90, 240, 150, fill='orange') # vykreslí to oranžový balón ktorý trochu prekrije modrý balón
canvas.create_oval(220, 90, 280, 150, fill='yellow') # vykreslí to žltý balón ktorý trochu prekrije oranžový balón
canvas.create_oval(260, 90, 320, 150, fill='pink') # vykreslí to ružový balón ktorý trochu prekrije žltý balón
canvas.create_oval(300, 90, 360, 150, fill='red') # vykreslí to červený balón ktorý trochu prekrije ružový balón

canvas.create_line(50, 150, 180, 330) # vykreslí to čiaru ktorá ide od stredu zeleného balónu smerom dole
canvas.create_line(90, 150, 180, 330) # vykreslí to čiaru ktorá ide od stredu limetkovo zeleného balónu smerom dole
canvas.create_line(130, 150, 180, 330) # vykreslí to čiaru ktorá ide od stredu fialového balónu smerom dole
canvas.create_line(170, 150, 180, 330) # vykreslí to čiaru ktorá ide od stredu modrého balónu smerom dole
canvas.create_line(210, 150, 180, 330) # vykreslí to čiaru ktorá ide od stredu oranžového balónu smerom dole
canvas.create_line(250, 150, 180, 330) # vykreslí to čiaru ktorá ide od stredu žltého balónu smerom dole
canvas.create_line(290, 150, 180, 330) # vykreslí to čiaru ktorá ide od stredu ružového balónu smerom dole
canvas.create_line(330, 150, 180, 330) # vykreslí to čiaru ktorá ide od stredu červeného balónu smerom dole
