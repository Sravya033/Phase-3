def BFS(start,graph,visited):
    visited.append(start)
    for ne in graph[start]:
        if ne not in visited:
            BFS(ne,graph,visited)
    return visited


graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","E"],
    "D":["B","E"],
    "E":["C","D"]

}
print(BFS("A",graph,[]))