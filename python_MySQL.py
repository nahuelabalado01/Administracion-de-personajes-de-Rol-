import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def cambioValor(gen):
    gen = str(gen).strip()
    if gen == "1":
        return "-5"
    elif gen == "2" or gen == "3":
        return "-4"
    elif gen == "4" or gen == "5":
        return "-3"
    elif gen == "6" or gen == "7":
        return "-2"
    elif gen == "8" or gen == "9":
        return "-1"
    elif gen == "10" or gen == "11":
        return "+0"
    elif gen == "12" or gen == "13":
        return "+1"
    elif gen == "14" or gen == "15":
        return "+2"
    elif gen == "16" or gen == "17":
        return "+3"
    elif gen == "18" or gen == "19":
        return "+4"
    elif gen == "20":
        return "+5"
    else:
        return ""

class FormularioClientes():

    def Formulario(): 
        try:
            base = Tk()
            base.geometry("1400x500")
            base.title("Formulario")
            
            grupBox = LabelFrame(base, text="Datos del PERSONAJE", font=("Times New Roman",15), padx=5, pady=5)
            grupBox.grid(row=0, column=0, padx=10, pady=10)
                
            Label(grupBox, text="Nombre:", width=13, font=("Times New Roman",12)).grid(row=0, column=0)
            texBoxId = Entry(grupBox)
            texBoxId.grid(row=0, column=1, padx=5, pady=5)
            
            # --- Fuerza ---
            Label(grupBox, text="Fuerza", width=13, font=("Times New Roman",12)).grid(row=1, column=0)
            seleccionFuerza = tk.StringVar(value="10")
            comboF = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionFuerza)
            comboF.grid(row=1, column=1, padx=5, pady=5)
            labelMejoraF = Label(grupBox, text=cambioValor(seleccionFuerza.get()), width=13, font=("Times New Roman",12))
            labelMejoraF.grid(row=1, column=3)

            # --- Destreza ---
            Label(grupBox, text="Destreza", width=13, font=("Times New Roman",12)).grid(row=2, column=0)
            seleccionDestreza = tk.StringVar(value="10")
            comboD = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionDestreza)
            comboD.grid(row=2, column=1, padx=5, pady=5)
            labelMejoraD = Label(grupBox, text=cambioValor(seleccionDestreza.get()), width=13, font=("Times New Roman",12))
            labelMejoraD.grid(row=2, column=3)

            # --- Constitucion ---
            Label(grupBox, text="Constitución", width=13, font=("Times New Roman",12)).grid(row=3, column=0)
            seleccionConstitucion = tk.StringVar(value="10")
            comboC = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionConstitucion)
            comboC.grid(row=3, column=1, padx=5, pady=5)
            labelMejoraC = Label(grupBox, text=cambioValor(seleccionConstitucion.get()), width=13, font=("Times New Roman",12))
            labelMejoraC.grid(row=3, column=3)

            # --- Sabiduria ---
            Label(grupBox, text="Sabiduria", width=13, font=("Times New Roman",12)).grid(row=4, column=0)
            seleccionSabiduria = tk.StringVar(value="10")
            comboS = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionSabiduria)
            comboS.grid(row=4, column=1, padx=5, pady=5)
            labelMejoraS = Label(grupBox, text=cambioValor(seleccionSabiduria.get()), width=13, font=("Times New Roman",12))
            labelMejoraS.grid(row=4, column=3)

            # --- inteligencia ---
            Label(grupBox, text="Inteligencia", width=13, font=("Times New Roman",12)).grid(row=5, column=0)
            seleccionInteligencia = tk.StringVar(value="10")
            comboI = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionInteligencia)
            comboI.grid(row=5, column=1, padx=5, pady=5)
            labelMejoraI = Label(grupBox, text=cambioValor(seleccionInteligencia.get()), width=13, font=("Times New Roman",12))
            labelMejoraI.grid(row=5, column=3)

            # --- Carisma ---
            Label(grupBox, text="Carisma", width=13, font=("Times New Roman",12)).grid(row=6, column=0)
            seleccionCarisma = tk.StringVar(value="10")
            comboCh = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionCarisma)
            comboCh.grid(row=6, column=1, padx=5, pady=5)
            labelMejoraCh = Label(grupBox, text=cambioValor(seleccionCarisma.get()), width=13, font=("Times New Roman",12))
            labelMejoraCh.grid(row=6, column=3)


            # --- Funciones de actualización ---
            def actualizar_fuerza(event):
                labelMejoraF.config(text=cambioValor(seleccionFuerza.get()))

            def actualizar_destreza(event):
                labelMejoraD.config(text=cambioValor(seleccionDestreza.get()))

            def actualizar_Constitucion(event):
                labelMejoraC.config(text=cambioValor(seleccionConstitucion.get()))

            def actualizar_sabiduria(event):
                labelMejoraS.config(text=cambioValor(seleccionSabiduria.get()))

            def actualizar_inteligencia(event):
                labelMejoraI.config(text=cambioValor(seleccionInteligencia.get()))

            def actualizar_Carisma(event):
                labelMejoraCh.config(text=cambioValor(seleccionCarisma.get()))

            comboC.bind("<<ComboboxSelected>>", actualizar_Constitucion)
            comboF.bind("<<ComboboxSelected>>", actualizar_fuerza)
            comboD.bind("<<ComboboxSelected>>", actualizar_destreza)
            comboCh.bind("<<ComboboxSelected>>", actualizar_Carisma)
            comboI.bind("<<ComboboxSelected>>", actualizar_inteligencia)
            comboS.bind("<<ComboboxSelected>>", actualizar_sabiduria)


            Button(grupBox,text="Guardar",width=10).grid(row=7,column=0)
            Button(grupBox,text="Modificar",width=10).grid(row=7,column=1)
            Button(grupBox,text="Eliminar",width=10).grid(row=7,column=2)

            # --- Listas ---
            grupBox = LabelFrame(base, text="Lista de PERSONAJES", font=("Times New Roman",15), padx=5, pady=5)
            grupBox.grid(row=0, column=1, padx=10, pady=10)

            # --- Frame contenedor ---
            frame_tabla = Frame(grupBox)
            frame_tabla.pack(fill="both", expand=True)

            # --- Scrollbars ---
            scroll_y = Scrollbar(frame_tabla, orient="vertical")
            scroll_x = Scrollbar(frame_tabla, orient="horizontal")

            # --- Treeview ---
            tree = ttk.Treeview(
                frame_tabla,
                columns=("Nombre", "Fuerza","Destreza","Constitucion","Sabiduria","Inteligencia","Carisma"),
                show='headings',
                height=10,
                yscrollcommand=scroll_y.set,
                xscrollcommand=scroll_x.set
            )

            # --- Configurar Scroll ---
            scroll_y.config(command=tree.yview)
            scroll_x.config(command=tree.xview)
            scroll_y.pack(side="right", fill="y")
            scroll_x.pack(side="bottom", fill="x")

            tree.pack(fill="both", expand=True)

            # --- Configurar columnas ---
            for col in ("Nombre", "Fuerza","Destreza","Constitucion","Sabiduria","Inteligencia","Carisma"):
                tree.heading(col, text=col)
                tree.column(col, width=120, anchor="center")





            base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz:", error)

    Formulario()
