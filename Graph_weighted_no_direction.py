class weightedEdge():
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self):
        return str(self.start)+'-'+str(self.end)+'('+str(self.weight)+')'


class EdgeWeightedGraph():
    def __init__(self, V, Edges):
        self.V = V
        self.E = 0
        self.mat = {}
        for i in range(V):
            self.mat[i] = []
        for each in Edges:
            self.addEdge(each[0], each[1], each[2])

    def addEdge(self, start, end, weight):
        if start not in self.mat or end not in self.mat:
            raise ValueError("start or end not in this graph")
        else:
            self.mat[start].insert(0, weightedEdge(start, end, weight))
            self.mat[end].insert(0,weightedEdge(end, start, weight))
            self.E += 1


    def adj(self, v):
        if v not in self.mat:
            raise ValueError("wrong v")
        return self.mat[v]


    def LazyPrimMST(self):
        pass


if __name__ == "__main__":

    Edges = [[4, 5, 0.35], [4, 7, 0.37], [5,7,0.28],[0,7,0.16],[1,5,0.32],[0,4,0.38],[2,3,0.17],[1,7,0.19],[0,2,0.26],[1,2,0.36],[1,3,0.29],[2,7,0.34],
             [6,2,0.4],[3,6,0.52],[6,0,0.58],[6,4,0.93]]
    G = EdgeWeightedGraph(8, Edges)
    print(G.mat)
    print(G.E)
    print(G.adj(0))
