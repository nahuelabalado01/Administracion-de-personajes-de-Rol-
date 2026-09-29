import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from contextlib import closing
from pathlib import Path

DB_PATH = Path(__file__).with_name("personajes.db")


def inicializar_db():
    with closing(sqlite3.connect(DB_PATH)) as conexion:
        with conexion:
            conexion.execute(
                """
                CREATE TABLE IF NOT EXISTS personajes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    fuerza INTEGER NOT NULL,
                    destreza INTEGER NOT NULL,
                    constitucion INTEGER NOT NULL,
                    sabiduria INTEGER NOT NULL,
                    inteligencia INTEGER NOT NULL,
                    carisma INTEGER NOT NULL
                )
                """
            )


def obtener_personajes():
    with closing(sqlite3.connect(DB_PATH)) as conexion:
        conexion.row_factory = sqlite3.Row
        return conexion.execute(
            """
            SELECT id, nombre, fuerza, destreza, constitucion,
                   sabiduria, inteligencia, carisma
            FROM personajes
            ORDER BY id
            """
        ).fetchall()


def insertar_personaje(datos):
    with closing(sqlite3.connect(DB_PATH)) as conexion:
        with conexion:
            conexion.execute(
                """
                INSERT INTO personajes (
                    nombre, fuerza, destreza, constitucion,
                    sabiduria, inteligencia, carisma
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                datos,
            )


def actualizar_personaje(personaje_id, datos):
    with closing(sqlite3.connect(DB_PATH)) as conexion:
        with conexion:
            conexion.execute(
                """
                UPDATE personajes
                SET nombre = ?, fuerza = ?, destreza = ?, constitucion = ?,
                    sabiduria = ?, inteligencia = ?, carisma = ?
                WHERE id = ?
                """,
                (*datos, personaje_id),
            )


def borrar_personaje(personaje_id):
    with closing(sqlite3.connect(DB_PATH)) as conexion:
        with conexion:
            conexion.execute("DELETE FROM personajes WHERE id = ?", (personaje_id,))


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

    @staticmethod
    def Formulario():
        base = Tk()
        base.geometry("1400x500")
        base.title("Formulario")

        try:
            inicializar_db()
        except sqlite3.Error as error:
            messagebox.showerror("Error de base de datos", str(error), parent=base)
            base.destroy()
            return
            
        grupBox = LabelFrame(base, text="Datos del PERSONAJE", font=("Times New Roman",15), padx=5, pady=5)
        grupBox.grid(row=0, column=0, padx=10, pady=10)
        formularioBox = grupBox
                
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


        registro_seleccionado = {"id": None}

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

        def obtener_datos_formulario():
            nombre = texBoxId.get().strip()
            atributos = (
                seleccionFuerza.get(),
                seleccionDestreza.get(),
                seleccionConstitucion.get(),
                seleccionSabiduria.get(),
                seleccionInteligencia.get(),
                seleccionCarisma.get(),
            )
            if not nombre:
                messagebox.showwarning("Dato requerido", "Ingresa el nombre del personaje.", parent=base)
                return None
            if any(not atributo for atributo in atributos):
                messagebox.showwarning("Dato requerido", "Selecciona todos los atributos.", parent=base)
                return None
            try:
                valores = tuple(int(atributo) for atributo in atributos)
            except ValueError:
                messagebox.showwarning("Dato inválido", "Los atributos deben ser números del 1 al 20.", parent=base)
                return None
            if any(not 1 <= valor <= 20 for valor in valores):
                messagebox.showwarning("Dato inválido", "Los atributos deben estar entre 1 y 20.", parent=base)
                return None
            return (nombre, *valores)

        def limpiar_formulario():
            registro_seleccionado["id"] = None
            texBoxId.delete(0, END)
            for seleccion in (
                seleccionFuerza,
                seleccionDestreza,
                seleccionConstitucion,
                seleccionSabiduria,
                seleccionInteligencia,
                seleccionCarisma,
            ):
                seleccion.set("10")
            for etiqueta in (labelMejoraF, labelMejoraD, labelMejoraC, labelMejoraS, labelMejoraI, labelMejoraCh):
                etiqueta.config(text=cambioValor("10"))

        def refrescar_tabla():
            for elemento in tree.get_children():
                tree.delete(elemento)
            try:
                for personaje in obtener_personajes():
                    tree.insert(
                        "",
                        END,
                        iid=str(personaje["id"]),
                        values=(
                            personaje["nombre"],
                            personaje["fuerza"],
                            personaje["destreza"],
                            personaje["constitucion"],
                            personaje["sabiduria"],
                            personaje["inteligencia"],
                            personaje["carisma"],
                        ),
                    )
            except sqlite3.Error as error:
                messagebox.showerror("Error de base de datos", str(error), parent=base)

        def seleccionar_personaje(event):
            if event.widget is not tree:
                return
            seleccion = tree.selection()
            if not seleccion:
                return
            registro_seleccionado["id"] = int(seleccion[0])
            valores = tree.item(seleccion[0], "values")
            texBoxId.delete(0, END)
            texBoxId.insert(0, valores[0])
            for variable, valor in zip(
                (
                    seleccionFuerza,
                    seleccionDestreza,
                    seleccionConstitucion,
                    seleccionSabiduria,
                    seleccionInteligencia,
                    seleccionCarisma,
                ),
                valores[1:],
            ):
                variable.set(valor)
            for etiqueta, variable in zip(
                (labelMejoraF, labelMejoraD, labelMejoraC, labelMejoraS, labelMejoraI, labelMejoraCh),
                (
                    seleccionFuerza,
                    seleccionDestreza,
                    seleccionConstitucion,
                    seleccionSabiduria,
                    seleccionInteligencia,
                    seleccionCarisma,
                ),
            ):
                etiqueta.config(text=cambioValor(variable.get()))

        def guardar_personaje():
            datos = obtener_datos_formulario()
            if datos is None:
                return
            try:
                insertar_personaje(datos)
                refrescar_tabla()
                limpiar_formulario()
            except sqlite3.Error as error:
                messagebox.showerror("Error de base de datos", str(error), parent=base)

        def modificar_personaje():
            personaje_id = registro_seleccionado["id"]
            if personaje_id is None:
                messagebox.showwarning("Selecciona un personaje", "Selecciona un personaje de la lista para modificarlo.", parent=base)
                return
            datos = obtener_datos_formulario()
            if datos is None:
                return
            try:
                actualizar_personaje(personaje_id, datos)
                refrescar_tabla()
                limpiar_formulario()
            except sqlite3.Error as error:
                messagebox.showerror("Error de base de datos", str(error), parent=base)

        def eliminar_personaje():
            personaje_id = registro_seleccionado["id"]
            if personaje_id is None:
                messagebox.showwarning("Selecciona un personaje", "Selecciona un personaje de la lista para eliminarlo.", parent=base)
                return
            if not messagebox.askyesno("Confirmar eliminación", "¿Quieres eliminar este personaje?", parent=base):
                return
            try:
                borrar_personaje(personaje_id)
                refrescar_tabla()
                limpiar_formulario()
            except sqlite3.Error as error:
                messagebox.showerror("Error de base de datos", str(error), parent=base)

        tree.bind("<<TreeviewSelect>>", seleccionar_personaje)
        Button(formularioBox,text="Guardar",width=10, command=guardar_personaje).grid(row=7,column=0)
        Button(formularioBox,text="Modificar",width=10, command=modificar_personaje).grid(row=7,column=1)
        Button(formularioBox,text="Eliminar",width=10, command=eliminar_personaje).grid(row=7,column=2)

        refrescar_tabla()
        base.mainloop()


if __name__ == "__main__":
    FormularioClientes.Formulario()
