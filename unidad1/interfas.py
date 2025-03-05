import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def guardar_info():
    genero = entrada_genero.get()
    autor = entrada_autor.get()
    volumenes = entrada_volumenes.get()
    tema_principal = entrada_tema.get("1.0", tk.END).strip()

    if genero and autor and volumenes and tema_principal:
        
        archivo = filedialog.asksaveasfile(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if archivo:
            
            archivo.write(f"Género: {genero}\n")
            archivo.write(f"Autor: {autor}\n")
            archivo.write(f"Número de volúmenes: {volumenes}\n")
            archivo.write(f"Tema principal: {tema_principal}\n")
            archivo.close()  # Cerrar el archivo
            messagebox.showinfo("Éxito", "Información guardada correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")


ventana = tk.Tk()
ventana.title("Literatura del Manga")
ventana.geometry("400x400")

tk.Label(ventana, text="Género:").pack(pady=5)
entrada_genero = tk.Entry(ventana, width=50)
entrada_genero.pack(pady=5)

tk.Label(ventana, text="Autor:").pack(pady=5)
entrada_autor = tk.Entry(ventana, width=50)
entrada_autor.pack(pady=5)

tk.Label(ventana, text="Número de volúmenes:").pack(pady=5)
entrada_volumenes = tk.Entry(ventana, width=50)
entrada_volumenes.pack(pady=5)

tk.Label(ventana, text="Tema principal:").pack(pady=5)
entrada_tema = tk.Text(ventana, height=5, width=50)
entrada_tema.pack(pady=5)

boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_info)
boton_guardar.pack(pady=20)

ventana.mainloop()
