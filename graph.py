
#3/18/23
#to define a Graph data structure and implement breadth-first and depth-first search algorithms on that graph.


from queue import Queue

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self): 
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key): # Add a vertex with the given key to the graph
        self.numVertices += 1
        new_vertex = Vertex(key)
        self.vertList[key] = new_vertex
        return new_vertex

    def getVertex(self, n): # Get the vertex object with the given key
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList.values()

    def addEdge(self, f, t, weight=0): # Add a directed edge with the given weight from vertex f to vertex t
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def breadth_first_search(self, s): # Perform a breadth-first search of the graph starting at vertex s
        visited = set()
        queue = []
        path = []
        start = self.vertList[s]
        visited.add(start)
        queue.append(start)
        path.append(start.id)
        while queue:
            v = queue.pop(0)
            for u in v.connectedTo.keys():
                if u not in visited:
                    visited.add(u)
                    queue.append(u)
                    path.append(u.id)
            v.color = 'black'
        return path[:len(self.vertList)]
    # return only the first len(self.vertList) elements of the path
    
    def depth_first_search(self): # Perform a depth-first search of the graph
        for v in self.vertList.values():
            v.color = 'white'
        path = [] # check the order of vertices traversed by DFS
        for v in self.vertList.values():
            if v.color == 'white':
                self.DFS(v.id, path)
        return path
    
    def DFS(self, vid, path): # Helper method for depth-first search
        v = self.vertList[vid]
        v.color = 'gray'
        path.append(v.id)
        for u in v.connectedTo.keys():
            if u.color == 'white':
                self.DFS(u.id, path)
        v.color = 'black'




if __name__ == '__main__':

    g = Graph()
    for i in range(6):
        g.addVertex(i)
        #print(g.addVertex(i))
        
    g.addEdge(0,1)
    g.addEdge(0,5)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,4)
    g.addEdge(5,2)

    # for v in g:
    #     print(v)

    # print(g)
    # assert (g.getVertex(0) in g) == True
    # assert (g.getVertex(6) in g) == False
    # print(g.getVertex(2) in g)
    # print(g.getVertex(6) in g)
        
    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]
    
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]
    
  
