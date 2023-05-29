graph = {
    '2': ['1', '3'],
    '1': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}
# visited=[]
# queue=[]

# def bfs(visited,graph,node):
#     visited.append(node)
#     queue.append(node)
#     while queue:
#         m=queue.pop(0)
#         print(m,end=" ")
#         for neighbor in graph:
#             if neighbor not in visited:
#                 visited.append(neighbor)
#                 queue.append(neighbor)

# print("Following is the BFS result:\n")

# bfs(visited,graph,'2')


def bfs_recursive(graph, queue, visited):
    if not queue:
        return

    node = queue.pop(0)
    print(node) 

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    bfs_recursive(graph, queue, visited)

# Example usage
graph = {
    '2': ['1', '3'],
    '1': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

starting_node = '2'
visited_nodes = set([starting_node])
node_queue = [starting_node]

bfs_recursive(graph, node_queue, visited_nodes)
