import tkinter as tk
from tkinter import messagebox

def verificar_numero():
    #Obtener el numero ingresado por el usuario.
    try:
        numero = int(entry.get())
    
        #Determinar si el número es par o impar.
        if numero % 2 == 0:
            resultado = "El número es par."
        else:
            resultado = "El número es impar."

    #Mostrar el restultado en un cuadro de mensaje
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número valido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Verificador de número Par o Impar")

# Crear un label
label = tk.Label(ventana, text = "¿En que número estas pensando?")
label.pack(pady=10)

# Crea un entry para que el usuario ingrese el número
entry = tk.Entry(ventana)
entry.pack(pady=5)

# Crea un boton para verificar el número
boton = tk.Button(ventana, text="Verificar", command=verificar_numero)
boton.pack(pady=10)

#Iniciar el bucle principal de la ventana
ventana.mainloop()
