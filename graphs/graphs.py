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
    
    # return all users
    def show_users(self):
        return self.gdict.keys()