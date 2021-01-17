from priority_queue_impl import PriorityQueueImpl
from node import Node

code = """A, B, 4
A, C, 7
A, D, 3
D, E, 3
B, E, 1
B, C, 3
C, F, 1
C, E, 1
E, F, 4"""

textFile = open("graphs.txt", "w")
textFile.write(code)
textFile.close()

textFile = open("graphs.txt", "r")
lines = textFile.read()
lines = lines.split("\n")

graphs = {}
distant = {}

for line in lines:
    aux = line.split(", ")
    if graphs.get(aux[0]) is None:
        graphs[aux[0]] = []
    distant[aux[0]] = float('inf')
    distant[aux[1]] = float('inf')
    graphs[aux[0]].append(Node(aux[1], int(aux[2])))

pq = PriorityQueueImpl()

camino = {}
pq.push(Node("A", 0), 0)
distant["A"] = 0
while not pq.empty():
    nodeAct = pq.pop()
    if graphs.get(nodeAct.dest) is None:
        continue
    for nodeAdy in graphs.get(nodeAct.dest):
        if (distant[nodeAct.dest] + nodeAdy.distant) < distant[nodeAdy.dest]:
            distant[nodeAdy.dest] = distant[nodeAct.dest] + nodeAdy.distant
            camino[nodeAdy.dest] = nodeAct.dest
            pq.push(Node(nodeAdy.dest, distant[nodeAdy.dest]), distant[nodeAdy.dest])

nodeStart = "A"
nodeFinal = "E"
print(camino)
while not camino.get(nodeFinal) is None:
    print(nodeFinal, "<--", camino.get(nodeFinal))
    nodeFinal = camino.get(nodeFinal)
