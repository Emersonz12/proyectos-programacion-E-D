import tkinter as tk
import re
from tkinter import messagebox


def Validar_Letras(Value):
    Patron = re.compile("^[A-Za-zÁ-Úá-úñÑ ]*$")
    Resultado = Patron.match(Value) is not None
    return Resultado


def Validar_Numeros(Value):
    Patron = re.compile("^[0-9]+$")  
    Resultado = Patron.match(Value) is not None
    return Resultado


def Evento_Presionar_Tecla(event):
    global Texto_Validar_Nombre
    if Validar_Letras(Nombre.get()):
        Texto_Validar_Nombre = ""
    else:
        Texto_Validar_Nombre = "Solo se permiten letras"
    LabelValidaciónNombre.config(text=Texto_Validar_Nombre)


def guardar_info():
    genero = entrada_genero.get()
    autor = entrada_autor.get()
    volumenes = entrada_volumenes.get()
    tema_principal = entrada_tema.get("1.0", tk.END).strip()

    if not Validar_Numeros(volumenes):
        messagebox.showwarning("Formato no admitido", "Por favor, ingresa un número válido en 'Número de volúmenes'.")
        return

    if not Validar_Letras(genero):
        messagebox.showwarning("Formato no admitido", "Por favor, ingresa un género válido (solo letras).")
        return

    if not Validar_Letras(autor):
        messagebox.showwarning("Formato no admitido", "Por favor, ingresa un autor válido (solo letras).")
        return

    if genero and autor and volumenes and tema_principal and Validar_Letras(Nombre.get()):
        
        messagebox.showinfo("Éxito", "Información guardada correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos correctamente.")


VentanaPrincipal = tk.Tk()
VentanaPrincipal.title("Ventana Principal")
VentanaPrincipal.geometry("400x600")


Nombre = tk.StringVar(VentanaPrincipal)
LabelNombre = tk.Label(VentanaPrincipal, text="Nombre")
EntryNombre = tk.Entry(VentanaPrincipal, textvariable=Nombre)
LabelValidaciónNombre = tk.Label(VentanaPrincipal, text="")

LabelNombre.pack()
EntryNombre.bind("<KeyRelease>", Evento_Presionar_Tecla)
EntryNombre.pack()
LabelValidaciónNombre.pack()


tk.Label(VentanaPrincipal, text="Género:").pack(pady=5)
entrada_genero = tk.Entry(VentanaPrincipal, width=50)
entrada_genero.pack(pady=5)

tk.Label(VentanaPrincipal, text="Autor:").pack(pady=5)
entrada_autor = tk.Entry(VentanaPrincipal, width=50)
entrada_autor.pack(pady=5)

tk.Label(VentanaPrincipal, text="Número de volúmenes:").pack(pady=5)
entrada_volumenes = tk.Entry(VentanaPrincipal, width=50)
entrada_volumenes.pack(pady=5)

tk.Label(VentanaPrincipal, text="Tema principal:").pack(pady=5)
entrada_tema = tk.Text(VentanaPrincipal, height=5, width=50)
entrada_tema.pack(pady=5)

boton_guardar = tk.Button(VentanaPrincipal, text="Guardar", command=guardar_info)
boton_guardar.pack(pady=20)

VentanaPrincipal.mainloop()
