import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
  def __init__(self):
    self.grafo = {}

  def add_vertice(self, v1, v2):
    if v1 in self.grafo:
      self.grafo[v1].append(v2)
    else:
      self.grafo[v1] = [v2]

    if v2 in self.grafo:
      self.grafo[v2].append(v1)
    else:
      self.grafo[v2] = [v1]

  def mostra_grafo(self):
    for k, v in self.grafo.items():
      #vizinhos = " -> ".join(map(str, self.grafo[v]))
      print(f"Vertice {k} : {v}")

  def teste(self):
    print(self.grafo.values())
    print(self.grafo.keys())
    print(self.grafo.items())

  def getVizinhos(self, a):
    vizinhos = self.grafo.get(a)
    return vizinhos
  
  def excluiRep(self, lista):
    lista_mod = lista.copy()
    for elemento in lista_mod:
      if elemento in LE:
        lista_mod.remove(elemento)
    for elemento in lista_mod:
      if elemento in LNE:
        lista_mod.remove(elemento)
    for elemento in lista_mod:
      if elemento in BSS:
        lista_mod.remove(elemento)
    return lista_mod
  
  def getDic(self):
    a = self.grafo
    return a
    

grafo = Grafo()

grafo.add_vertice("A", "B")
grafo.add_vertice("A", "C")
grafo.add_vertice("A", "D")
grafo.add_vertice("B", "E")
grafo.add_vertice("B", "F")
grafo.add_vertice("C", "F")
grafo.add_vertice("C", "G")
grafo.add_vertice("E", "H")
grafo.add_vertice("E", "I")
grafo.add_vertice("F", "U")

LE = ['A']
LNE = ['A']
BSS = []
EC = 'A'

a = grafo.getVizinhos(EC)
b = grafo.excluiRep(a)
c = grafo.getDic()

print(a)  
print(b) 
print(c) 

G = nx.DiGraph(c)
# Defina uma cor para cada nó em um dicionário
#node_colors = {'A': 'red', 'B': 'skyblue', 'C': 'skyblue', 'D': 'skyblue', 'E': 'skyblue', 'F': 'skyblue','G': 'yellow', 'H': 'skyblue','I': 'skyblue', 'U': 'skyblue'}
cores = ['red' if n in LE else 'skyblue' for n in G.nodes()]
pos = {'A': (1, 2), 'B': (-1, 1.5), 'C': (1, 1.5), 'D': (3, 1.5), 'E': (-2, 1), 'F': (0, 1), 'G': (2, 1), 'H': (-3, 0.5), 'I': (-1, 0.5), 'U': (1, 0.5)}  # Layout do grafo
nx.draw(G, pos, with_labels=True, node_size=500, node_color=cores, font_size=12, font_color='black', font_weight='bold', arrowsize=15)
plt.show()



"""
while not LNE:
  a = grafo.getVizinhos(EC)
  if EC == 'G':
    print(f"Objetivo encontrado: {EC}")
    
  for elemento in a:
    if elemento in LE and LNE and BSS:
      a.remove(elemento)

"""

