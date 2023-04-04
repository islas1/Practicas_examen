#contraseña
from tkinter import *
import tkinter as tk

cuenta=1
def iniciar_cuenta():
    usuario1 = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if cuenta == 1 :
        
        def iniciar_sesion():
            contrasena1 = contrasena1_usuario.get()
            contraseña = contrasena1
            if contraseña != contrasena:
                resultado.config(text="Muy bien, contraseña actualizada",bg="beige")
            else:
                 resultado.config(text="La contraseña debe ser diferente a la anterior, por favor intentelo de nuevo.",bg="beige")

        ventana2 = tk.Tk()
        ventana2.configure(background="beige")
        ventana2.title("Cambio de contraseña :)")
        ventana2.configure(padx=300)
        ventana2.configure(pady=50)
        # Entrada para la contraseña
        mi_label3 = tk.Label(ventana2,
                             text="Su accedio a su cuenta sin su autorizacion, por favor cambie su contraseña",
                             bg="beige")
        mi_label3.pack()
        contrasena1_usuario = tk.Entry(ventana2, show="#")
        contrasena1_usuario.pack()

        # Botones
        iniciar_sesion = tk.Button(ventana2, text="Cambiar contraseña", command=iniciar_sesion)
        iniciar_sesion.pack(padx=40, pady=40)
        salir = tk.Button(ventana2, text="Cancelar cambio", command=ventana2.quit)
        salir.pack()

        # Widgets
        resultado = tk.Label(ventana2, text="")
        resultado.pack(pady=90)

        ventana2.mainloop()
    else:
        resultado.config(text="Nombre de usuario o contraseña incorrectos")

ventana6 = Tk()

ventana6.configure(bg="beige")
ventana6.title("Inicio de sesión")
ventana6.configure(padx=200)

# Entrada para el nombre de usuario y la contraseña
mi_label= Label(text="Ingrese su usuario",bg="beige")
mi_label.pack()
nombre_usuario = Tk=Entry(ventana6)
nombre_usuario.pack(pady=40)

mi_label2= Label(text="Ingrese Contraseña",bg="beige")
mi_label2.pack()
contrasena_usuario = Tk=Entry(ventana6, show="*")
contrasena_usuario.pack()

# Botones
iniciar_cuenta = Tk=Button(ventana6, text="Iniciar sesión", command=iniciar_cuenta)
iniciar_cuenta.pack(padx=20, pady=20)
salir = Tk=Button(ventana6, text="Cerrar", command=ventana6.quit)
salir.pack()

# Widgets
resultado = Tk=Label(ventana6, text="")
resultado.pack(pady=90)

ventana6.mainloop()

