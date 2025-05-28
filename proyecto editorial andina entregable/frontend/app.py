import tkinter as tk
from tkinter import messagebox, ttk
import threading
import requests
import time

API_BASE = "http://127.0.0.1:8000/api"

# ------------------- FUNCIONES DE RESPALDO ------------------- #

def generar_respaldo_autores():
    try:
        response = requests.get(f"{API_BASE}/autores/")
        if response.status_code == 200:
            data = response.json()
            with open("respaldo_autores.txt", "w", encoding="utf-8") as f:
                for autor in data:
                    f.write(f"Nombre: {autor['nombre']}\n")
                    f.write(f"Nacionalidad: {autor['nacionalidad']}\n")
                    f.write(f"Edad: {autor['edad']}\n")
        else:
            print("Error al obtener autores")
    except:
        print("No se pudo generar respaldo de autores")

def generar_respaldo_libros():
    try:
        response = requests.get(f"{API_BASE}/libros/")
        if response.status_code == 200:
            data = response.json()
            with open("respaldo_libros.txt", "w", encoding="utf-8") as f:
                for libro in data:
                    f.write(f"Título: {libro['titulo']}\n")
                    f.write(f"Género: {libro['genero']}\n")
                    f.write(f"Páginas: {libro['paginas']}\n")
                    f.write(f"Año: {libro['anio']}\n")
        else:
            print("Error al obtener libros")
    except:
        print("No se pudo generar respaldo de libros")

def respaldo_periodico():
    while True:
        generar_respaldo_autores()
        generar_respaldo_libros()
        time.sleep(10)

# ------------------- FUNCIONES AUXILIARES ------------------- #

def crear_entrada_y_etiqueta(frame, texto, row):
    label = tk.Label(frame, text=texto, bg=frame["bg"], anchor="w", width=15)
    label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(frame, width=30)
    entry.grid(row=row, column=1, padx=5, pady=5)
    return entry

def buscar_por_id(endpoint, item_id):
    try:
        r = requests.get(f"{API_BASE}/{endpoint}/{item_id}/")
        if r.status_code == 200:
            return r.json()
        return None
    except:
        return None

# ------------------- VENTANAS DE GESTIÓN ------------------- #

def ventana_autores():
    win = tk.Toplevel()
    win.title("Gestión de Autores")
    win.configure(bg="#d0f0c0")
    win.geometry("460x360")

    frame = tk.Frame(win, bg="#d0f0c0")
    frame.pack(padx=10, pady=10)

    nombre = crear_entrada_y_etiqueta(frame, "Nombre:", 0)
    nacionalidad = crear_entrada_y_etiqueta(frame, "Nacionalidad:", 1)
    edad = crear_entrada_y_etiqueta(frame, "Edad:", 2)

    id_buscar = crear_entrada_y_etiqueta(frame, "ID a buscar:", 3)
    id_eliminar = crear_entrada_y_etiqueta(frame, "ID a eliminar:", 4)

    def registrar():
        data = {
            "nombre": nombre.get(),
            "nacionalidad": nacionalidad.get(),
            "edad": edad.get()
        }

        # Evitar duplicados por nombre
        r = requests.get(f"{API_BASE}/autores/")
        if r.status_code == 200:
            autores = r.json()
            for autor in autores:
                if autor["nombre"].lower() == data["nombre"].lower():
                    messagebox.showwarning("Duplicado", "El autor ya existe.")
                    return

        r = requests.post(f"{API_BASE}/autores/", json=data)
        if r.status_code == 201:
            messagebox.showinfo("Éxito", "Autor registrado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo registrar el autor")

    def buscar():
        autor_id = id_buscar.get()
        autor = buscar_por_id("autores", autor_id)
        if autor:
            messagebox.showinfo("Autor encontrado",
                                f"Nombre: {autor['nombre']}\n"
                                f"Nacionalidad: {autor['nacionalidad']}\n"
                                f"Edad: {autor['edad']}")
        else:
            messagebox.showerror("Error", "Autor no encontrado")

    def eliminar():
        autor_id = id_eliminar.get()
        r = requests.delete(f"{API_BASE}/autores/{autor_id}/")
        if r.status_code == 204:
            messagebox.showinfo("Eliminado", "Autor eliminado con éxito")
        else:
            messagebox.showerror("Error", "No se pudo eliminar")

    def ver_autores():
        lista_win = tk.Toplevel()
        lista_win.title("Lista de Autores")
        lista_win.configure(bg="#f0f8ff")
        tree = ttk.Treeview(lista_win, columns=("ID", "Nombre", "Nacionalidad", "Edad"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True)

        response = requests.get(f"{API_BASE}/autores/")
        if response.status_code == 200:
            for autor in response.json():
                tree.insert("", "end", values=(autor["id"], autor["nombre"], autor["nacionalidad"], autor["edad"]))

    tk.Button(win, text="Registrar", command=registrar, bg="#98fb98").pack(pady=5)
    tk.Button(win, text="Buscar por ID", command=buscar, bg="#e0ffff").pack(pady=5)
    tk.Button(win, text="Eliminar por ID", command=eliminar, bg="#ff7f7f").pack(pady=5)
    tk.Button(win, text="Ver Autores", command=ver_autores, bg="#add8e6").pack(pady=5)

def ventana_libros():
    win = tk.Toplevel()
    win.title("Gestión de Libros")
    win.configure(bg="#f9f9f9")
    win.geometry("500x430")

    frame = tk.Frame(win, bg="#f9f9f9")
    frame.pack(padx=10, pady=10)

    titulo = crear_entrada_y_etiqueta(frame, "Título:", 0)
    genero = crear_entrada_y_etiqueta(frame, "Género:", 1)
    paginas = crear_entrada_y_etiqueta(frame, "Páginas:", 2)
    anio = crear_entrada_y_etiqueta(frame, "Año:", 3)

    id_buscar = crear_entrada_y_etiqueta(frame, "ID a buscar:", 4)
    id_eliminar = crear_entrada_y_etiqueta(frame, "ID a eliminar:", 5)

    def registrar():
        data = {
            "titulo": titulo.get(),
            "genero": genero.get(),
            "paginas": paginas.get(),
            "anio": anio.get()
        }

        # Evitar duplicados por título
        r = requests.get(f"{API_BASE}/libros/")
        if r.status_code == 200:
            libros = r.json()
            for libro in libros:
                if libro["titulo"].lower() == data["titulo"].lower():
                    messagebox.showwarning("Duplicado", "El libro ya existe.")
                    return

        r = requests.post(f"{API_BASE}/libros/", json=data)
        if r.status_code == 201:
            messagebox.showinfo("Éxito", "Libro registrado correctamente")
        else:
            messagebox.showerror("Error", "No se pudo registrar el libro")

    def buscar():
        libro_id = id_buscar.get()
        libro = buscar_por_id("libros", libro_id)
        if libro:
            messagebox.showinfo("Libro encontrado",
                                f"Título: {libro['titulo']}\n"
                                f"Género: {libro['genero']}\n"
                                f"Páginas: {libro['paginas']}\n"
                                f"Año: {libro['anio']}")
        else:
            messagebox.showerror("Error", "Libro no encontrado")

    def eliminar_libro():
        libro_id = id_eliminar.get()
        r = requests.delete(f"{API_BASE}/libros/{libro_id}/")
        if r.status_code == 204:
            messagebox.showinfo("Eliminado", "Libro eliminado con éxito")
        else:
            messagebox.showerror("Error", "No se pudo eliminar")

    def ver_libros():
        lista_win = tk.Toplevel()
        lista_win.title("Lista de Libros")
        lista_win.configure(bg="#fffef2")
        tree = ttk.Treeview(lista_win, columns=("ID", "Título", "Género", "Páginas", "Año"), show="headings")
        for col in tree["columns"]:
            tree.heading(col, text=col)
        tree.pack(fill=tk.BOTH, expand=True)

        response = requests.get(f"{API_BASE}/libros/")
        if response.status_code == 200:
            for libro in response.json():
                tree.insert("", "end", values=(libro["id"], libro["titulo"], libro["genero"], libro["paginas"], libro["anio"]))

    tk.Button(win, text="Registrar", command=registrar, bg="#98fb98").pack(pady=5)
    tk.Button(win, text="Buscar por ID", command=buscar, bg="#e0ffff").pack(pady=5)
    tk.Button(win, text="Eliminar por ID", command=eliminar_libro, bg="#ff7f7f").pack(pady=5)
    tk.Button(win, text="Ver Libros", command=ver_libros, bg="#add8e6").pack(pady=5)

# ------------------- VENTANA PRINCIPAL ------------------- #

root = tk.Tk()
root.title("Editorial Andina - Gestión")
root.geometry("350x250")
root.configure(bg="#ddeeff")

frame = tk.Frame(root, bg="#ddeeff")
frame.pack(pady=20)

tk.Label(frame, text="Menú Principal", bg="#ddeeff", font=("Arial", 16)).pack(pady=10)
tk.Button(frame, text="Gestión de Autores", command=ventana_autores, width=25, bg="#ccffcc").pack(pady=5)
tk.Button(frame, text="Gestión de Libros", command=ventana_libros, width=25, bg="#ffffcc").pack(pady=5)

# Iniciar respaldo automático
threading.Thread(target=respaldo_periodico, daemon=True).start()

root.mainloop()
