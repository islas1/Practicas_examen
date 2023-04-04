import tkinter as tk


def adios():
    print("Adios, hasta luego")

class MenuScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Menú")

        #menú superior
        self.menu_bar = tk.Menu(self.master)
        self.master.config(bg="skyblue",)
        self.master.config(menu=self.menu_bar)
        
        #opciones
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Promedio de una materia ", command=self.open_file)
        self.file_menu.add_command(label="Mayor y menor número de una lista ", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Cerrar el programa ", command=self.quit_program)
        self.menu_bar.add_cascade(label="Calcular", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Copiar", command=self.copy)
        self.edit_menu.add_command(label="Pegar", command=self.paste)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Decirle hola c:", command=self.sal_file)
        self.file_menu.add_command(label="No decirle hola :c", command=self.sal2_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.quit_program)
        self.menu_bar.add_cascade(label="Saludar al programador", menu=self.file_menu)

        #widgets
        self.label = tk.Label(self, text=" Hola queridisimo usuario ")
        self.label.config(bg="white")
        self.label.pack(pady=20)
        self.button = tk.Button(self, text="Si presionas aqui se cae tu dedo", command=self.press_button)
        self.button.config(bg="white")
        self.button.pack()

        self.pack()

    def sal_file(self):
        print("El usuario te dice hola c:")

    def sal2_file(self):
        print("El usuario no te dijo hola :c")

    def open_file(self):
        materia =input("¿De que materia deseas calcular tu promedio? -> ")
        print(  )
        print("Bien, calculemos tu promedio final de "+materia)
        print(  )
        print("Por favor ingresa la calificacion de tus 4 parciales ")
        print("Introduce números enteros, ejemplo : 9.5 = 95 :) ")
        print("-----------------")
        print(  )
        suma=0
        num=0
        for i in range (1,5):
            num = float (input("-> "))
            suma=suma+num
            prom=suma//4
            promstring = f"{prom}"
        print("tu promedio final de "+materia+ " es "+promstring)
        adios()

    def save_file(self):
        a=True
        while a==True :
            try:
                cant = int(input("¿cuantos números desea ingresar?: -> "))
                print(  )
            except ValueError:
                print("Error, Debe ingresar caractéres válidos.")
            else:
                lista_numeros = []
                for i in range(cant):
                    jja= i
                    numero = float(input("-> "))
                    lista_numeros.append(numero)
                break
                #finally:   
                print("Gracias por utilizar este codigo :D")
        maximo= max(lista_numeros)
        lista_mayorstr=f"{maximo}"
        print("El mayor número es "+lista_mayorstr)
        minimo= min(lista_numeros)
        lista_menorstr=f"{minimo}"
        print("El menor número es "+lista_menorstr)
    
    def quit_program(self):
        print("adiooO0o0ooOOO0oo00s")
        self.master.quit()

    def copy(self):
        print("¿Copiar? eso no se hace bro")

    def paste(self):
        print("Pegar? nomas a mi vieja >:)")

    def press_button(self):
        print("Yaaa se te cayo tu dedo :c")

root = tk.Tk()
root.geometry("500x400")
app = MenuScreen(root)
app.mainloop()
