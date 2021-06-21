class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # add connection
    def add_connection(self, node, connection):
        self.gdict[node].append(connection)
    
    # remove connection
    def remove_connection(self, node, connection):  
        self.gdict[node].remove(connection)
    
    # total connections
    def count_connections(self, node):
         return len(self.gdict[node])

    # show connections
    def show_connections(self, node):
        return self.gdict[node]

    # add new node / user
    def add_user(self, node):
        self.gdict[node] = []

    # count all users
    def count_users(self):
        return len(self.gdict)
    
    # return all users -- traversal
    def show_users(self):
        return self.gdict.keys()
   
    # BFS Traversal
    def BFSTraversal(self, node):
        queue = [node]
        visited = [node]
        while queue:
            # pop element at 0th index
            dVertex = queue.pop(0)
            print(dVertex, end="")
            print("\tConnections:", len(self.gdict[dVertex]))
            for aVertex in self.gdict[dVertex]:
                # push adjacent nodes in the queue if it is not visited
                if aVertex not in visited:
                    queue.append(aVertex)
                    # mark as visited
                    visited.append(aVertex)
                  
     # DFS Traversal
    def DFSTraversal(self, node):
        stack = [node]
        visited = [node]
        while stack:
            # pop element at top/ last index
            popVertex = stack.pop()
            print(popVertex, end="")
            print("\tConnections:", len(self.gdict[popVertex]))
            for aVertex in self.gdict[popVertex]:
                # push adjacent nodes in the stack if it is not visited
                if aVertex not in visited:
                    stack.append(aVertex)
                    # mark as visited
                    visited.append(aVertex)
        
    
                
        