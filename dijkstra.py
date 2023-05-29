graph = { 
    0: [(1, 4), (2, 5), (3, 6), (4, 7)],
    1: [(0, 1)],
    2: [(0, 5), (3, 8), (4, 4)],
    3: [(0, 6), (2, 8), (4, 2)],
    4: [(0, 7), (2, 4), (3, 2)]
}
# takes the graph and the starting node
# returns a list of distances from the starting node to every other node
Inf=99999
def Dijkstra(graph, start):
    l = len(graph)
    
    # initialize all node distances as infinite
    dist = [Inf for _ in range(l)]
    
    # set the distance of starting node as 0
    dist[start] = 0
    
    # create a list that indicates if a node is visited or not
    vis = [False for _ in range(l)]
    
    # iterate over all the nodes
    for _ in range(l):
        
        # set u=-1 to indicate a current starting node
        u = -1
        
        # iterate over all the nodes to check the status of the visit 
        for x in range(l):
            # now if the 'x' node is not visited yet or the distance we have currently for it is less than the distance to the start node then update the current node as the 'x'
            if not vis[x] and (u == -1 or dist[x] < dist[u]):
                u = x
                
        # check if we have visited all the nodes or we haven't reached the node
        if dist[u] == Inf:
            break
            
        # set the currently running node as visited
        vis[u] = True
        
       # now if the distance of the current node + the distance to the node we're visiting is less than the prior distance of the node we're visiting then update that distance.
        for v, d in graph[u]:
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d
                
    # now at last return the list which contains the shortest path to each node from that given node            
    print("SHORTEST DISTANCE OF EVERY VERTEX FROM '0' is as follows\n")
    for i in range(5):
        print("From VERTEX ",i," : ",dist[i])
    
Dijkstra(graph,0)
