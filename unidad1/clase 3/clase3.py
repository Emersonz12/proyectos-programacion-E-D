from tkinter import Frame, Tk 
from tkinter.messagebox import askyesno

VentanaPrincipal = Tk()
VentanaPrincipal.title("Prueba de Eventos")

def accionclick(event):
    frame.focus_set()
    print("clicked at",event.x,event.y)

def preciosar_tecla(event):
    print("pressed", repr(event.char))

frame = Frame(VentanaPrincipal, width=500, height=500)
frame.bind("<Button-1>", accionclick)
frame.bind("<Key>", preciosar_tecla)

def el_usuario_quiere_salir():
    if askyesno("salir","desea salir de la aplicacion?"):
        VentanaPrincipal.destroy()

frame.pack()

VentanaPrincipal.protocol("WM_DELETE_WINDOW",el_usuario_quiere_salir)
VentanaPrincipal.mainloop()
