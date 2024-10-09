import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class GrafoEuler:
    def __init__(self):
        self.grafo = nx.Graph()
    
    # Genera un grafo aleatorio conexo con el número de nodos
    def generar_grafo_conexo(self, nodos):
        self.grafo.clear()
        self.grafo.add_nodes_from(range(nodos))
        
        for i in range(1, nodos):
            u = random.randint(0, i - 1)  
            self.grafo.add_edge(i, u)
        

    # Dibuja el grafo generado y muestra el grado de cada nodo
    def dibujar_grafo(self):
        pos = nx.spring_layout(self.grafo)
        
        # Obtener los grados de los nodos
        etiquetas_nodos = {nodo: str(self.grafo.degree(nodo)) for nodo in self.grafo.nodes()}
        
        nx.draw(self.grafo, pos, with_labels=True, labels=etiquetas_nodos, node_color="lightblue", font_weight='bold', node_size=700)
        plt.draw() 

    # Función para verificar si el grafo es euleriano
    def es_euleriano(self):
        # Primero, verificar si el grafo es conexo
        if not nx.is_connected(self.grafo):
            return "El grafo no es conexo, por lo tanto no tiene camino ni circuito euleriano."
        
        # Contar cuántos vértices tienen grado impar
        grados_impares = [v for v in self.grafo.nodes() if self.grafo.degree(v) % 2 != 0]
        num_impares = len(grados_impares)

        if num_impares == 0:
            return "El grafo tiene un circuito euleriano"
        elif num_impares == 2:
            return "El grafo tiene un camino euleriano"
        else:
            return "El grafo no tiene ni circuito ni camino euleriano"


    def iniciar(self):
        nodos = int(input("¿Cuántos nodos quieres en el grafo? "))
        self.generar_grafo_conexo(nodos)
        self.dibujar_grafo()
        print(self.es_euleriano())
        plt.show()  
if __name__ == "__main__":
    grafo_euler = GrafoEuler()
    grafo_euler.iniciar()
