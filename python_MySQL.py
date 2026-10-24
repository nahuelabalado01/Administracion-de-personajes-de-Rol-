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
                    raza TEXT NOT NULL DEFAULT 'Humano',
                    clase TEXT NOT NULL DEFAULT 'Guerrero',
                    fuerza INTEGER NOT NULL,
                    destreza INTEGER NOT NULL,
                    constitucion INTEGER NOT NULL,
                    sabiduria INTEGER NOT NULL,
                    inteligencia INTEGER NOT NULL,
                    carisma INTEGER NOT NULL
                )
                """
            )
            columnas = {
                columna[1]
                for columna in conexion.execute("PRAGMA table_info(personajes)")
            }
            if "raza" not in columnas:
                conexion.execute(
                    "ALTER TABLE personajes ADD COLUMN raza TEXT NOT NULL DEFAULT 'Humano'"
                )
            if "clase" not in columnas:
                conexion.execute(
                    "ALTER TABLE personajes ADD COLUMN clase TEXT NOT NULL DEFAULT 'Guerrero'"
                )


def obtener_personajes():
    with closing(sqlite3.connect(DB_PATH)) as conexion:
        conexion.row_factory = sqlite3.Row
        return conexion.execute(
            """
            SELECT id, nombre, raza, clase, fuerza, destreza, constitucion,
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
                    nombre, raza, clase, fuerza, destreza, constitucion,
                    sabiduria, inteligencia, carisma
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                datos,
            )


def actualizar_personaje(personaje_id, datos):
    with closing(sqlite3.connect(DB_PATH)) as conexion:
        with conexion:
            conexion.execute(
                """
                UPDATE personajes
                SET nombre = ?, raza = ?, clase = ?, fuerza = ?, destreza = ?, constitucion = ?,
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
    try:
        gen = int(str(gen).strip())
    except ValueError:
        return ""
    return f"{(gen - 10) // 2:+d}"

bonificaciones = {
        "Fuerza": {
            "Enano De las Montañas": 2,
            "Humano": 1,
            "Draconido": 2,
            "Semiorco": 2,
        },
        "Destreza": {
            "Elfo": 2,
            "Humano": 1,
            "Mediano": 2,
            "Gnomo del Bosque": 1,
        },
        "Constitucion": {
            "Gnomo de las Rocas": 1,
            "Humano": 1,
            "Enano": 2,
            "Semiorco": 1,
            "Mediano Fornido": 1,
        },
        "Sabiduria": {
            "Humano": 1,
            "Elfo del Bosque": 1,
            "Enano de las Colinas": 1,
        },
        "Inteligencia": {
            "Humano": 1,
            "Elfo Alto": 1,
            "Gnomo": 2,
            "Tiefling": 1,
        },
        "Carisma": {
            "Humano": 1,
            "Tiefling": 2,
            "Draconido": 1,
            "Mediano pies ligeros": 1,
            "Semielfo": 2,
            "Drow": 1,
        },
    }



def Mejora_Valor(gen, raza, clase, atributo):
    valor = int(gen)
    bonificacion = bonificaciones.get(atributo, {}).get(raza, 0)
    return valor + bonificacion


class FormularioClientes():

    @staticmethod
    def Formulario():
        base = Tk()
        base.geometry("1200x700")
        base.title("Formulario")

        try:
            inicializar_db()
        except sqlite3.Error as error:
            messagebox.showerror("Error de base de datos", str(error), parent=base)
            base.destroy()
            return

        contenedor = Frame(base)
        contenedor.pack(fill="both", expand=True)

        canvas = Canvas(contenedor, highlightthickness=0)
        scroll_vertical = Scrollbar(
            contenedor, orient=VERTICAL, command=canvas.yview
        )
        scroll_horizontal = Scrollbar(
            contenedor, orient=HORIZONTAL, command=canvas.xview
        )
        canvas.configure(
            yscrollcommand=scroll_vertical.set,
            xscrollcommand=scroll_horizontal.set,
        )
        canvas.grid(row=0, column=0, sticky="nsew")
        scroll_vertical.grid(row=0, column=1, sticky="ns")
        scroll_horizontal.grid(row=1, column=0, sticky="ew")
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)

        contenido = Frame(canvas)
        canvas.create_window((0, 0), window=contenido, anchor="nw")
        contenido.bind(
            "<Configure>",
            lambda event: canvas.configure(scrollregion=canvas.bbox("all")),
        )

        grupBox = LabelFrame(contenido, text="Datos del PERSONAJE", font=("Times New Roman",15), padx=5, pady=5)
        grupBox.grid(row=0, column=0, padx=10, pady=10)
        formularioBox = grupBox
                
        Label(grupBox, text="Nombre:", width=13, font=("Times New Roman",12)).grid(row=0, column=0)
        texBoxId = Entry(grupBox)
        texBoxId.grid(row=0, column=1, padx=5, pady=5)

        Label(grupBox, text="Raza:", width=13, font=("Times New Roman",12)).grid(row=0, column=2)
        seleccionRaza = tk.StringVar(value="Humano")
        razas = (
            "Draconido",
            "Drow",
            "Elfo",
            "Elfo Alto",
            "Elfo del Bosque",
            "Enano",
            "Enano De las Montañas",
            "Enano de las Colinas",
            "Gnomo",
            "Gnomo de las Rocas",
            "Gnomo del Bosque",
            "Humano",
            "Mediano",
            "Mediano Fornido",
            "Mediano pies ligeros",
            "Semielfo",
            "Semiorco",
            "Tiefling",
        )
        comboRaza = ttk.Combobox(
            grupBox,
            values=razas,
            textvariable=seleccionRaza,
            state="readonly",
            width=22,
        )
        comboRaza.grid(row=0, column=3, padx=5, pady=5)

        Label(grupBox, text="Clase:", width=13, font=("Times New Roman",12)).grid(row=0, column=4)
        seleccionClase = tk.StringVar(value="Guerrero")
        clases = (
            "Bárbaro",
            "Bardo",
            "Brujo",
            "Clérigo",
            "Druida",
            "Explorador",
            "Guerrero",
            "Hechicero",
            "Mago",
            "Monje",
            "Paladín",
            "Pícaro",
        )
        comboClase = ttk.Combobox(
            grupBox,
            values=clases,
            textvariable=seleccionClase,
            state="readonly",
            width=18,
        )
        comboClase.grid(row=0, column=5, padx=5, pady=5)
            
        # --- Fuerza ---
        Label(grupBox, text="Fuerza", width=13, font=("Times New Roman",12)).grid(row=1, column=0)
        seleccionFuerza = tk.StringVar(value="10")
        comboF = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionFuerza)
        comboF.grid(row=1, column=1, padx=5, pady=5)
        labelMejoraF = Label(grupBox, text="", width=13, font=("Times New Roman",12))
        labelMejoraF.grid(row=1, column=3)

        # --- Destreza ---
        Label(grupBox, text="Destreza", width=13, font=("Times New Roman",12)).grid(row=2, column=0)
        seleccionDestreza = tk.StringVar(value="10")
        comboD = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionDestreza)
        comboD.grid(row=2, column=1, padx=5, pady=5)
        labelMejoraD = Label(grupBox, text="", width=13, font=("Times New Roman",12))
        labelMejoraD.grid(row=2, column=3)

        # --- Constitucion ---
        Label(grupBox, text="Constitución", width=13, font=("Times New Roman",12)).grid(row=3, column=0)
        seleccionConstitucion = tk.StringVar(value="10")
        comboC = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionConstitucion)
        comboC.grid(row=3, column=1, padx=5, pady=5)
        labelMejoraC = Label(grupBox, text="", width=13, font=("Times New Roman",12))
        labelMejoraC.grid(row=3, column=3)

        # --- Sabiduria ---
        Label(grupBox, text="Sabiduria", width=13, font=("Times New Roman",12)).grid(row=4, column=0)
        seleccionSabiduria = tk.StringVar(value="10")
        comboS = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionSabiduria)
        comboS.grid(row=4, column=1, padx=5, pady=5)
        labelMejoraS = Label(grupBox, text="", width=13, font=("Times New Roman",12))
        labelMejoraS.grid(row=4, column=3)

        # --- inteligencia ---
        Label(grupBox, text="Inteligencia", width=13, font=("Times New Roman",12)).grid(row=5, column=0)
        seleccionInteligencia = tk.StringVar(value="10")
        comboI = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionInteligencia)
        comboI.grid(row=5, column=1, padx=5, pady=5)
        labelMejoraI = Label(grupBox, text="", width=13, font=("Times New Roman",12))
        labelMejoraI.grid(row=5, column=3)

        # --- Carisma ---
        Label(grupBox, text="Carisma", width=13, font=("Times New Roman",12)).grid(row=6, column=0)
        seleccionCarisma = tk.StringVar(value="10")
        comboCh = ttk.Combobox(grupBox, values=[str(i) for i in range(1, 21)], textvariable=seleccionCarisma)
        comboCh.grid(row=6, column=1, padx=5, pady=5)
        labelMejoraCh = Label(grupBox, text="", width=13, font=("Times New Roman",12))
        labelMejoraCh.grid(row=6, column=3)


        variables_mejora = (
            (seleccionFuerza, labelMejoraF, "Fuerza"),
            (seleccionDestreza, labelMejoraD, "Destreza"),
            (seleccionConstitucion, labelMejoraC, "Constitucion"),
            (seleccionSabiduria, labelMejoraS, "Sabiduria"),
            (seleccionInteligencia, labelMejoraI, "Inteligencia"),
            (seleccionCarisma, labelMejoraCh, "Carisma"),
        )
        
        def actualizar_rangos(event=None):
            raza = seleccionRaza.get()

            atributos = (
                (comboF, "Fuerza"),
                (comboD, "Destreza"),
                (comboC, "Constitucion"),
                (comboS, "Sabiduria"),
                (comboI, "Inteligencia"),
                (comboCh, "Carisma")
            )

            for combo, atributo in atributos:
                bonificador = bonificaciones.get(atributo, {}).get(raza, 0)
                maximo = 20 - bonificador

                combo["values"] = [str(i) for i in range(1, maximo + 1)]

                try:
                    valor_actual = int(combo.get())
                except ValueError:
                    valor_actual = 10

                if valor_actual > maximo:
                    combo.set(str(maximo))
                elif valor_actual < 1:
                    combo.set("1")

        def actualizar_mejoras(event=None):
            for variable, etiqueta, atributo in variables_mejora:
                valor = Mejora_Valor(
                    variable.get(), seleccionRaza.get(), "", atributo
                )
                etiqueta.config(text=f"{valor} ({cambioValor(valor)})")
        
        def cambiar_raza(event=None):
            actualizar_rangos()
            actualizar_mejoras()

        comboRaza.bind("<<ComboboxSelected>>", cambiar_raza)
        for combo in (comboF, comboD, comboC, comboS, comboI, comboCh):
            combo.bind("<<ComboboxSelected>>", actualizar_mejoras)
        


        registro_seleccionado = {"id": None}

        # --- Listas ---
        grupBox = LabelFrame(contenido, text="Lista de PERSONAJES", font=("Times New Roman",15), padx=5, pady=5)
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
            columns=("Nombre", "Raza", "Clase", "Fuerza","Destreza","Constitucion","Sabiduria","Inteligencia","Carisma"),
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
        anchos_columnas = {
            "Nombre": 110,
            "Raza": 100,
            "Clase": 100,
            "Fuerza": 60,
            "Destreza": 70,
            "Constitucion": 85,
            "Sabiduria": 75,
            "Inteligencia": 85,
            "Carisma": 65,
        }
        for col, ancho in anchos_columnas.items():
            tree.heading(col, text=col)
            tree.column(col, width=ancho, minwidth=ancho, stretch=False, anchor="center")

        def obtener_datos_formulario():
            nombre = texBoxId.get().strip()
            raza = seleccionRaza.get()
            clase = seleccionClase.get()
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
            if not raza or not clase or any(not atributo for atributo in atributos):
                messagebox.showwarning("Dato requerido", "Selecciona una raza, una clase y todos los atributos.", parent=base)
                return None
            try:
                valores = tuple(int(atributo) for atributo in atributos)
            except ValueError:
                messagebox.showwarning("Dato inválido", "Los atributos deben ser números del 1 al 20.", parent=base)
                return None
            if any(not 1 <= valor <= 20 for valor in valores):
                messagebox.showwarning("Dato inválido", "Los atributos deben estar entre 1 y 20.", parent=base)
                return None
            return (nombre, raza, clase, *valores)

        def limpiar_formulario():
            registro_seleccionado["id"] = None
            texBoxId.delete(0, END)
            seleccionRaza.set("Humano")
            seleccionClase.set("Guerrero")
            for seleccion in (
                seleccionFuerza,
                seleccionDestreza,
                seleccionConstitucion,
                seleccionSabiduria,
                seleccionInteligencia,
                seleccionCarisma,
            ):
                seleccion.set("10")
            actualizar_mejoras()

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
                            personaje["raza"],
                            personaje["clase"],
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
            seleccionRaza.set(valores[1])
            seleccionClase.set(valores[2])
            for variable, valor in zip(
                (
                    seleccionFuerza,
                    seleccionDestreza,
                    seleccionConstitucion,
                    seleccionSabiduria,
                    seleccionInteligencia,
                    seleccionCarisma,
                ),
                valores[3:],
            ):
                variable.set(valor)
            actualizar_rangos()
            actualizar_mejoras()

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

