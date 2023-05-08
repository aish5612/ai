visited = set()

graph = {"A":["B","C","D"],  
   "B":["E"],  
   "C":["G","F"],  
   "D":["H"],  
   "E":["I"],  
   "F":["J"],  
   "G":["K"]}  

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end = "")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

dfs(graph, 'A', visited)


visited = []
q = []
def bfs(visited, graph, node):
    visited.append(node)
    q.append(node)
    while q:
        v = q.pop()
        print(v, end = " ")
        for u in graph[v]:
            if u not in visited:
                visited.append(u)
                q.append(u)
bfs(visited, graph, 'A')