import tkinter as tk
from tkinter import messagebox, ttk
import requests

API_URL = "http://localhost:8000/api/mangas/"

def buscar():
    manga_id = entry_id.get()
    if manga_id:
        response = requests.get(API_URL + manga_id + "/")
        if response.status_code == 200:
            data = response.json()
            entry_genero.delete(0, tk.END)
            entry_genero.insert(0, data['genero'])
            entry_autor.delete(0, tk.END)
            entry_autor.insert(0, data['autor'])
            entry_volumenes.delete(0, tk.END)
            entry_volumenes.insert(0, data['volumenes'])
            entry_tema.delete(0, tk.END)
            entry_tema.insert(0, data['tema_principal'])
        else:
            messagebox.showerror("Error", "Manga no encontrado")
    else:
        messagebox.showwarning("Aviso", "Debes ingresar un ID para buscar")

def guardar():
    data = {
        "genero": entry_genero.get(),
        "autor": entry_autor.get(),
        "volumenes": int(entry_volumenes.get()),
        "tema_principal": entry_tema.get()
    }
    response = requests.post(API_URL, json=data)
    if response.status_code in (200, 201):
        messagebox.showinfo("Éxito", "Manga guardado")
        cargar_tabla()
    else:
        messagebox.showerror("Error", "No se pudo guardar")
    limpiar_campos()

def actualizar():
    manga_id = entry_id.get()
    if manga_id:
        data = {
            "genero": entry_genero.get(),
            "autor": entry_autor.get(),
            "volumenes": int(entry_volumenes.get()),
            "tema_principal": entry_tema.get()
        }
        response = requests.put(API_URL + manga_id + "/", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Éxito", "Manga actualizado")
            cargar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo actualizar")
    limpiar_campos()

def eliminar():
    manga_id = entry_id.get()
    if manga_id:
        response = requests.delete(API_URL + manga_id + "/")
        if response.status_code == 204:
            messagebox.showinfo("Éxito", "Manga eliminado")
            cargar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo eliminar")
    limpiar_campos()

def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_volumenes.delete(0, tk.END)
    entry_tema.delete(0, tk.END)

def cargar_tabla():
    for fila in tabla.get_children():
        tabla.delete(fila)
    response = requests.get(API_URL)
    if response.status_code == 200:
        datos = response.json()
        for manga in datos:
            tabla.insert('', 'end', values=(
                manga['id'],
                manga['genero'],
                manga['autor'],
                manga['volumenes'],
                manga['tema_principal']
            ))
    else:
        messagebox.showerror("Error", "No se pudieron cargar los datos")


root = tk.Tk()
root.title("Gestión de Mangas")


tk.Label(root, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Button(root, text="Consultar por ID", command=buscar).grid(row=0, column=2)

tk.Label(root, text="Género").grid(row=1, column=0)
entry_genero = tk.Entry(root)
entry_genero.grid(row=1, column=1)

tk.Label(root, text="Autor").grid(row=2, column=0)
entry_autor = tk.Entry(root)
entry_autor.grid(row=2, column=1)

tk.Label(root, text="Volúmenes").grid(row=3, column=0)
entry_volumenes = tk.Entry(root)
entry_volumenes.grid(row=3, column=1)

tk.Label(root, text="Tema Principal").grid(row=4, column=0)
entry_tema = tk.Entry(root)
entry_tema.grid(row=4, column=1)


tk.Button(root, text="Guardar", command=guardar).grid(row=5, column=0)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=5, column=1)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=5, column=2)


tk.Button(root, text="Consultar Todos", command=cargar_tabla).grid(row=6, column=1, pady=10)


tabla = ttk.Treeview(root, columns=("ID", "Genero", "Autor", "Volumenes", "Tema"), show='headings')
tabla.heading("ID", text="ID")
tabla.heading("Genero", text="Género")
tabla.heading("Autor", text="Autor")
tabla.heading("Volumenes", text="Volúmenes")
tabla.heading("Tema", text="Tema Principal")
tabla.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
