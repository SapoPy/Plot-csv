import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('TkAgg')

# Variables globales para almacenar las opciones de columnas
column_options = []

# Función para generar el gráfico
def plot_disaggregation(file_csv, x, y, z, x_label, y_label, z_label, dx, dy):
    try:
        df_clean = pd.read_csv(file_csv, header=1)
        df_filtered = df_clean[[x, y, z]]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X = df_filtered[x].values
        Y = df_filtered[y].values
        Z = np.zeros_like(X)
        dz = df_filtered[z].values

        ax.bar3d(X, Y, Z, float(dx), float(dy), dz)

        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_zlabel(z_label)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Función para cargar archivo CSV y actualizar las opciones de columnas
def load_file():
    file_csv = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_csv:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_csv)
        
        # Leer el archivo CSV y actualizar las opciones de columnas
        try:
            df = pd.read_csv(file_csv, header=1)
            global column_options
            column_options = list(df.columns)

            # Actualizar los menús desplegables con las nuevas opciones
            update_option_menu(x_column_var, x_option_menu)
            update_option_menu(y_column_var, y_option_menu)
            update_option_menu(z_column_var, z_option_menu)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo CSV:\n{e}")

# Función para actualizar los menús desplegables
def update_option_menu(variable, option_menu):
    menu = option_menu["menu"]
    menu.delete(0, "end")
    for option in column_options:
        menu.add_command(label=option, command=lambda value=option: variable.set(value))

# Función que toma los inputs y llama a la función de gráfico
def generate_plot():
    file_csv = entry_file.get()
    x = x_column_var.get()
    y = y_column_var.get()
    z = z_column_var.get()
    x_label = entry_x_label.get()
    y_label = entry_y_label.get()
    z_label = entry_z_label.get()
    dx = entry_dx.get()
    dy = entry_dx.get()

    if file_csv and x and y and z and x_label and y_label and z_label and dx and dy:
        plot_disaggregation(file_csv, x, y, z, x_label, y_label, z_label, dx, dy)
    else:
        messagebox.showwarning("Input faltante", "Por favor, rellene todos los campos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de gráficos 3D")

# Elementos de la interfaz
label_file = tk.Label(root, text="Archivo CSV:")
label_file.grid(row=0, column=0, padx=10, pady=10)
entry_file = tk.Entry(root, width=40)
entry_file.grid(row=0, column=1, padx=10, pady=10)
btn_file = tk.Button(root, text="Cargar", command=load_file)
btn_file.grid(row=0, column=2, padx=10, pady=10)

# Columna X con menú desplegable
label_x = tk.Label(root, text="Columna X:")
label_x.grid(row=1, column=0, padx=10, pady=10)
x_column_var = tk.StringVar(root)
x_option_menu = tk.OptionMenu(root, x_column_var, "")
x_option_menu.grid(row=1, column=1, padx=10, pady=10)

# Nombre personalizado para el eje X
label_x_label = tk.Label(root, text="Nombre Eje X:")
label_x_label.grid(row=1, column=2, padx=10, pady=10)
entry_x_label = tk.Entry(root, width=20)
entry_x_label.grid(row=1, column=3, padx=10, pady=10)

# Columna Y con menú desplegable
label_y = tk.Label(root, text="Columna Y:")
label_y.grid(row=2, column=0, padx=10, pady=10)
y_column_var = tk.StringVar(root)
y_option_menu = tk.OptionMenu(root, y_column_var, "")
y_option_menu.grid(row=2, column=1, padx=10, pady=10)

# Nombre personalizado para el eje Y
label_y_label = tk.Label(root, text="Nombre Eje Y:")
label_y_label.grid(row=2, column=2, padx=10, pady=10)
entry_y_label = tk.Entry(root, width=20)
entry_y_label.grid(row=2, column=3, padx=10, pady=10)

# Columna Z con menú desplegable
label_z = tk.Label(root, text="Columna Z:")
label_z.grid(row=3, column=0, padx=10, pady=10)
z_column_var = tk.StringVar(root)
z_option_menu = tk.OptionMenu(root, z_column_var, "")
z_option_menu.grid(row=3, column=1, padx=10, pady=10)

# Nombre personalizado para el eje Z
label_z_label = tk.Label(root, text="Nombre Eje Z:")
label_z_label.grid(row=3, column=2, padx=10, pady=10)
entry_z_label = tk.Entry(root, width=20)
entry_z_label.grid(row=3, column=3, padx=10, pady=10)

# Valores de dx y dy
label_dx = tk.Label(root, text="Ancho de barras (dx):")
label_dx.grid(row=4, column=0, padx=10, pady=10)
entry_dx = tk.Entry(root, width=20)
entry_dx.grid(row=4, column=1, padx=10, pady=10)

label_dy = tk.Label(root, text="Profundidad de barras (dy):")
label_dy.grid(row=4, column=2, padx=10, pady=10)
entry_dy = tk.Entry(root, width=20)
entry_dy.grid(row=4, column=3, padx=10, pady=10)

# Botón para generar el gráfico
btn_generate = tk.Button(root, text="Generar Gráfico", command=generate_plot)
btn_generate.grid(row=5, column=1, padx=10, pady=10)

# Ejecutar la ventana
root.mainloop()
