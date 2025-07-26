
import math as mt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
headers = ('D','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')


archivo = open("Datos.txt", "r")

#Declaracion de variables
DistanciaA = 0
DistanciaB = 0
DistanciaC = 0
i = 0
n = 0
Total = 0
Existe = True
AgenteActual = 0
Agente = []
Z = 0
AgentesResultantes = []
Costo = []
DELTA_F = []
SubTour = [] 
SubTourm = []
AgenteResiduo = []
Agente.append(AgenteActual)
#Declaracion de arreglos
Coordenadax, Coordenaday = 2, 21;
CoordenadaCliente = [[0 for x in range(Coordenadax)] for y in range(Coordenaday)] 

Distanciax, Distanciay = 21, 21;
DistanciaCliente = [[0 for x in range(Distanciax)] for y in range(Distanciay)] 

#Lectura de Coordenadas 
for i in range(21):
    STRClienteX = archivo.readline()
    STRClienteY = archivo.readline()
    Cx = int(STRClienteX)
    Cy = int(STRClienteY)
    CoordenadaCliente[i][0] = Cx
    CoordenadaCliente[i][1] = Cy
    
archivo.close()



#Calcular distancia entre clientes
for i in range(21):
    DistanciaA1 = CoordenadaCliente[i][0]
    DistanciaB1 = CoordenadaCliente[i][1]
    for n in range(21):
        DistanciaA = DistanciaA1 - CoordenadaCliente[n][0]
        DistanciaB = DistanciaB1 - CoordenadaCliente[n][1]
        DistanciaC = mt.sqrt(pow(DistanciaA,2)+pow(DistanciaB,2))
        DistanciaCliente[i][n] = round(DistanciaC)


# --- ALGORITMO DE INSERCIÓN MÁS LEJANA (AJUSTA AQUÍ TU LÓGICA DE RUTA) ---
# Por ahora, solo se muestra la ruta secuencial como ejemplo. Sustituye por tu lógica real si es necesario.
Agente = list(range(21))
Total = 0
for i in range(len(Agente)-1):
    Total += DistanciaCliente[Agente[i]][Agente[i+1]]

# --- VISUALIZACIÓN EN UNA SOLA VENTANA CON PESTAÑAS ---
root = tk.Tk()
root.title("Resultados Computados - Inserción Más Lejana")
root.geometry("900x700")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Pestaña de la gráfica
frame_grafica = ttk.Frame(notebook)
notebook.add(frame_grafica, text="Gráfica de Ruta")

fig, ax = plt.subplots(figsize=(8, 8))
x_coords = [CoordenadaCliente[i][0] for i in Agente]
y_coords = [CoordenadaCliente[i][1] for i in Agente]
ax.plot(x_coords, y_coords, marker='o', linestyle='-', color='b', label='Ruta')
for idx, (x, y) in enumerate(zip(x_coords, y_coords)):
    ax.scatter(x, y, color='red')
    ax.text(x, y+1, str(Agente[idx]), fontsize=10, ha='center')
ax.set_title('Ruta de Inserción Más Lejana')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
ax.legend()
fig.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.draw()
canvas.get_tk_widget().pack(expand=True, fill="both")

# Pestaña de la tabla
frame_tabla = ttk.Frame(notebook)
notebook.add(frame_tabla, text="Tabla de Resultados")

tree = ttk.Treeview(frame_tabla, columns=("#1", "#2"), show="headings")
tree.heading("#1", text="Orden de Visita")
tree.heading("#2", text="Cliente (X, Y)")
for idx, cliente in enumerate(Agente):
    tree.insert("", "end", values=(idx+1, f"({CoordenadaCliente[cliente][0]}, {CoordenadaCliente[cliente][1]})"))
tree.pack(expand=True, fill="both", padx=10, pady=10)

label_total = tk.Label(frame_tabla, text=f"Costo total: {Total}", font=("Arial", 14, "bold"))
label_total.pack(pady=10)

root.mainloop()
    