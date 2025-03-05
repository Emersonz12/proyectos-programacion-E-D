import tkinter as tk 

ventanaPrincipal = tk.Tk()
nombre = tk.StringVar(ventanaPrincipal)
labelNombre = tk.Label(ventanaPrincipal, text="nombre")
entryNombre = tk.Entry(ventanaPrincipal, textvariable=nombre)
labelValidacionnombre = tk.Label(ventanaPrincipal, text= "")

def evento_presionar_tecla(event):
    print(nombre.get())

ventanaPrincipal.title("ventana principal ")
ventanaPrincipal.geometry("300x300")
labelNombre.pack()
entryNombre.bind("<keyRelease>", evento_presionar_tecla)
entryNombre.pack()
labelValidacionnombre.pack()


ventanaPrincipal.mainloop()  