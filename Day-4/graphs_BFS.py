def graph(start,arr):
    q=[start]
    visited=[start]
    while q:
        ele=q.pop(0)
        for i in arr[ele]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited

arr={
    "A":["B","C","D"],
    "B":["A","C"],
    "C":["D","B","A"],
    "D":["A","C"]
}
start="B"
print(graph(start,arr))