
graph={
    '1':['2','3'],
    '2':['4','5'],
    '3':['6','7'],
    '4':[],
    '5':[],
    '6':[],
    '7':[]
}

visited=set()
def dfs(visted,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for n in graph[node]:
            dfs(visited,graph,n)

print("Followiing is the result of DFS:")
dfs(visited,graph,'1')


