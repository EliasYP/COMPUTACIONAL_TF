import random
import networkx as nx
import matplotlib.pyplot as plt

# Solicitar tamaño de matriz al usuario
n = int(input("Ingrese el tamaño n de la matriz (entre 5 y 15): ")) 

while n < 5 or n > 15:
  n = int(input("Tamaño fuera de rango. Ingreselo nuevamente: "))

# Generar matriz simétrica aleatoria o ingresada
print("Desea generar la matriz aleatoriamente (1) o ingresar valores (2)?")
op = int(input())

if op == 1:
  matriz = [[random.randint(1,10) for i in range(n)] for j in range(n)]
else: 
  matriz = [[int(input(f"Ingrese elemento [{i},{j}]: ")) for i in range(n)] for j in range(n)]
  
for i in range(n):
  matriz[i][i] = 0
  for j in range(n):
    matriz[j][i] = matriz[i][j]
    
# Crear grafo a partir de la matriz    
G = nx.DiGraph()
G.add_nodes_from(range(n)) 

for i in range(n):
  for j in range(n):
    if matriz[i][j] > 0:
      G.add_edge(i,j,weight=matriz[i][j])
      
# Mostrar grafo      
pos = nx.spring_layout(G)
nx.draw(G, pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

# Calcular camino mínimo
origen = int(input("Ingrese vértice origen: "))
destino = int(input("Ingrese vértice destino: "))

camino_minimo = nx.dijkstra_path(G,origen,destino)
print(f"Camino mínimo: {camino_minimo}")