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
      print(f"Vertice {k} : {v}")

  def teste(self):
    print(self.grafo.values())
    print(self.grafo.keys())
    print(self.grafo.items())

  def getVizinhos(self, a):
    vizinhos = self.grafo.get(a)
    return vizinhos
  
  def excluiRep(self, vizinhos):
    lista_mod = vizinhos.copy()
    conjunto = set(LE).union(LNE).union(BSS)
    array_resultante = list(conjunto)
    
    for elemento in array_resultante:
      if elemento in lista_mod:
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

# Recebe o dicionario para desenhar o grafo
c = grafo.getDic()
G = nx.DiGraph(c)
pos = {'A': (1, 2), 'B': (-1, 1.5), 'C': (1, 1.5), 'D': (3, 1.5), 'E': (-2, 1), 'F': (0, 1), 'G': (2, 1), 'H': (-3, 0.5), 'I': (-1, 0.5), 'U': (1, 0.5)} 


print(f"LE: {LE} | LNE: {LNE} | BSS: {BSS} | EC: {EC} ")
while  len(LNE) != 0:
  cores = {}
  for v in G.nodes():
    if v in LE:
      cores[v] = 'red'
    elif v in BSS:
      cores[v] = 'purple'
    else:
      cores[v] = 'skyblue'

  nx.draw(G, pos, with_labels=True, node_size=500, node_color=[cores[n] for n in G.nodes()], font_size=12, font_color='black', font_weight='bold', arrowsize=15)
  plt.show()

  if EC == 'G':
    print(f"Objetivo encontrado: {EC}")
    plt.show()
    break
  
  # Pega os vizinhos de EC e remove os que ja estão em LE, LNE e BSS
  vizinhos = grafo.getVizinhos(EC)
  excluirNos = grafo.excluiRep(vizinhos)

  # Se EC não tem filhos
  if len(excluirNos) == 0:
    while (LE != 0) and (EC == LE[0]):
      # Acrescenta EC em BSS
      BSS.insert(0, EC)
      # Remove primeiro elemento de LE
      LE.pop(0)
      # Remove primeiro elemento de LNE
      LNE.pop(0)
      # EC recebe primeiro elemento de LNE
      EC = LNE[0]
      print(f"LE: {LE} | LNE: {LNE} | BSS: {BSS} | EC: {EC} ") 
      # Gera o grafo
      for v in G.nodes():
        if v in LE:
          cores[v] = 'red'
        elif v in BSS:
          cores[v] = 'purple'
        else:
          cores[v] = 'skyblue'
      nx.draw(G, pos, with_labels=True, node_size=500, node_color=[cores[n] for n in G.nodes()], font_size=12, font_color='black', font_weight='bold', arrowsize=15)
      plt.show()
    # Acrescenta EC a LE
    LE.insert(0, EC)
    print(f"LE: {LE} | LNE: {LNE} | BSS: {BSS} | EC: {EC} ")
    
  # Se EC tem filhos
  else:
    # Coloca filhos de EC (exceto nós ja em BSS, LE ou LNE) em LNE
    LNE = excluirNos + LNE
    # EC recebe primeiro elemento de LNE
    EC = LNE[0]
    # Acrescenta EC a LE
    LE.insert(0, EC)
    print(f"LE: {LE} | LNE: {LNE} | BSS: {BSS} | EC: {EC} ")

