#!/usr/bin/env python3 
#-*- coding: utf-8 -*-

import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




#Se crea el grafo
grafo = nx.Graph()
# Creamos una instancia de la clase Tk
ventana = tk.Tk()

# Establecemos el título de la ventana
ventana.title("Algoritmo de PRIM - Árbol recubridor minimal")

# Establecemos las dimensiones de la ventana
ventana.geometry("1000x650")

#Para que no se pueda ajustar ancho y alto de la ventana
ventana.resizable(False, False)

marco1 = tk.Frame(ventana, bd=5, relief="groove")
marco1.place(width=985, height=525, x=10, y=10)



fig1 = plt.figure()
canvas = FigureCanvasTkAgg(fig1, master=marco1)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)


def agregar_arista():

    arista = entry2.get()
    peso = entry3.get()

    # Si la arista es una cadena de longitud 2, entonces se agrega la arista al grafo
    if len(arista) == 2:
        vertice1, vertice2 = arista[0], arista[1]
        grafo.add_edge(vertice1, vertice2, weight=int(peso))

        #Se limpia el canvas
        canvas.figure.gca().cla() # Limpiar el canvas
        # Dibujamos el grafo en el canvas
        pos = nx.spring_layout(grafo)
        nx.draw(grafo, pos, ax=canvas.figure.gca())

        #Poner labels de los vertices
        labels = {v: v for v in grafo.nodes()}
        nx.draw_networkx_labels(grafo, pos, labels, font_size=10, font_color="black", font_weight="bold")

        #Poner labels de las aristas
        edge_labels = nx.get_edge_attributes(grafo, 'weight')
        nx.draw_networkx_edge_labels(grafo, pos, edge_labels, font_size=10, font_color="black")
        
        # Actualizamos el canvas
        canvas.draw()
        

    # Si la arista no es una cadena de longitud 2, se muestra un mensaje de error
    else:
        tk.messagebox.showerror("Error", "La arista debe ser una cadena de longitud 2")

def aplicar_prim():
    # Obtiene el vértice de inicio del usuario
   

    # Aplica el algoritmo de Prim para obtener el árbol de expansión mínimo
    arbol_expansion_minimo = nx.minimum_spanning_tree(grafo, weight='weight')

    # Dibuja el árbol de expansión mínimo en el mismo canvas que el grafo original
    canvas.figure.gca().cla()
    pos = nx.spring_layout(arbol_expansion_minimo)
    nx.draw(arbol_expansion_minimo, pos, ax=canvas.figure.gca())

    #Poner labels de los vertices
    labels = {v: v for v in arbol_expansion_minimo.nodes()}
    nx.draw_networkx_labels(arbol_expansion_minimo, pos, labels, font_size=10, font_color="white", font_weight="bold")

    #Poner labels de las aristas
    edge_labels = nx.get_edge_attributes(arbol_expansion_minimo, 'weight')
    nx.draw_networkx_edge_labels(arbol_expansion_minimo, pos, edge_labels, font_size=10, font_color="black")

    # Actualiza el canvas para que se muestre el nuevo dibujo
    canvas.draw()

   




# Agregamos los widgets debajo de los marcos

label2 = tk.Label(ventana, text="Arista")
label3 = tk.Label(ventana, text="Peso")


entry2 = tk.Entry(ventana,width=10)
entry3 = tk.Entry(ventana,width=10)


button2 = tk.Button(ventana, text="Agregar arista",command=agregar_arista)
button3 = tk.Button(ventana, text="Aplicar algoritmo de PRIM",command=aplicar_prim)
# Posicionamos los widgets debajo de los marcos



label2.place(x=10, y=590)
entry2.place(x=100, y=590)
label3.place(x=225, y=590)
entry3.place(x=275, y=590)
button2.place(x=400, y=590)



button3.place(x=610, y=590)

# Mostramos la ventana
ventana.mainloop()

