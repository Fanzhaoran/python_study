graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}
def DFS(graph, s):
    queue = []
    queue.append(s)
    receve = set()
    receve.add(s)
    while len(queue) > 0:
        element = queue.pop()
        nodes = graph[element]
        for i in nodes:
            
            if i not in receve:
                queue.append(i)
                receve.add(i)
        print(element)
# DFS(graph,"A")
