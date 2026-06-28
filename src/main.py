import tkinter as tk
from tkinter import messagebox
import random
import string


historial = []


def generar_contrasena():

    caracteres = ""

    if var_mayus.get():
        caracteres += string.ascii_uppercase
    if var_minus.get():
        caracteres += string.ascii_lowercase
    if var_num.get():
        caracteres += string.digits
    if var_sim.get():
        caracteres += string.punctuation

    if caracteres == "":
        messagebox.showwarning("Advertencia", "Selecciona al menos una opción")
        return

    try:
        longitud = int(entry_longitud.get())
        if longitud < 1:
            messagebox.showerror("Error", "La longitud debe ser mayor a 0")
            return
    except:
        messagebox.showerror("Error", "Ingresa un número válido")
        return

    password = "".join(random.choice(caracteres) for _ in range(longitud))

    resultado.delete(0, tk.END)
    resultado.insert(0, password)

    historial.append(password)
    actualizar_historial()

    evaluar(password)


def actualizar_historial():
    lista_historial.delete(0, tk.END)

    for i, p in enumerate(historial[-10:], 1):
        lista_historial.insert(tk.END, f"{i}. {p}")


def limpiar_historial():
    historial.clear()
    actualizar_historial()
    messagebox.showinfo("Historial", "Historial limpiado")


def evaluar(password):

    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        etiqueta.config(text="Seguridad: Baja")
    elif score <= 4:
        etiqueta.config(text="Seguridad: Media")
    else:
        etiqueta.config(text="Seguridad: Alta")


def copiar():

    texto = resultado.get()

    if texto.strip() == "":
        messagebox.showwarning("Aviso", "No hay contraseña generada")
        return

    ventana.clipboard_clear()
    ventana.clipboard_append(texto)

    messagebox.showinfo("Copiado", "Contraseña copiada")


# ================= UI =================

ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("520x600")
ventana.resizable(False, False)


tk.Label(ventana, text="GENERADOR DE CONTRASEÑAS", font=("Arial", 16, "bold")).pack(pady=10)


frame = tk.Frame(ventana)
frame.pack()


tk.Label(frame, text="Longitud:").grid(row=0, column=0)
entry_longitud = tk.Entry(frame, width=10)
entry_longitud.insert(0, "12")
entry_longitud.grid(row=0, column=1)


var_mayus = tk.BooleanVar(value=True)
var_minus = tk.BooleanVar(value=True)
var_num = tk.BooleanVar(value=True)
var_sim = tk.BooleanVar(value=True)


tk.Checkbutton(ventana, text="Mayúsculas", variable=var_mayus).pack()
tk.Checkbutton(ventana, text="Minúsculas", variable=var_minus).pack()
tk.Checkbutton(ventana, text="Números", variable=var_num).pack()
tk.Checkbutton(ventana, text="Símbolos", variable=var_sim).pack()


tk.Button(ventana, text="GENERAR CONTRASEÑA", command=generar_contrasena).pack(pady=10)


resultado = tk.Entry(ventana, width=40, font=("Arial", 12))
resultado.pack()


etiqueta = tk.Label(ventana, text="Seguridad:")
etiqueta.pack(pady=5)


tk.Button(ventana, text="COPIAR", command=copiar).pack(pady=5)


tk.Label(ventana, text="HISTORIAL (últimos 10)").pack()

lista_historial = tk.Listbox(ventana, width=40, height=6)
lista_historial.pack()


tk.Button(ventana, text="LIMPIAR HISTORIAL", command=limpiar_historial).pack(pady=5)


tk.Label(ventana, text="Proyecto Integrador", font=("Arial", 8)).pack(side="bottom", pady=10)


ventana.mainloop()
