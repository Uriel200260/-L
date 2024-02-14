import tkinter as tk
from tkinter import messagebox


def option1():
    messagebox.showinfo("Detalle 1", "Con mucho amor para ti mi amor\n Espero te guste")
    try:
        import Surpirse2
    except ImportError:
        print("No se pudo importar el archivo.")

def option2():
    messagebox.showinfo("Detalle 2", "Gracias por otro 14 de febrero contigo 🥰, TE AMO ❤, Disfruta el detalle ❣")
    #texto = tk.Label(text="¡Que esta flor ilumine tu dia,\n tal como tu sonrisa y tus ojos con mi vida!", font=("Arial", 19))
    #texto.pack(padx=7, pady=7)
    try:
        import Surprise1
    except ImportError:
        print("No se pudo importar el archivo.")

#def option3():
  #  messagebox.showinfo("Opción 3", "¡Seleccionaste la opción 3!")



# Crear la ventana principal
root = tk.Tk()
root.title("Menú Gráfico")

# Crear un marco para los botones
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Crear los botones del menú
button1 = tk.Button(frame, text="Detalle 1", command=option1)
button1.pack(fill=tk.X, padx=5, pady=5)


button2 = tk.Button(frame, text="Detalle 2", command=option2)
button2.pack(fill=tk.X, padx=5, pady=5)

#button3 = tk.Button(frame, text="Opción 3", command=option3)
#button3.pack(fill=tk.X, padx=5, pady=5)

button4 = tk.Button(frame, text="Salir", command=exit)
button4.pack(fill=tk.X, padx=5, pady=5)

if button1 != button1:
    option1()
if button2 != button2:
     option2()
# Ejecutar el bucle de eventos
root.mainloop()
