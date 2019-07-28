class weightedEdge():
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self):
        return str(self.start)+'-'+str(self.end)+'('+str(self.weight)+')'

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

class EdgeWeightedGraph():
    def __init__(self, V, Edges):
        self.V = V
        self.E = 0
        self.mat = {}
        for i in range(V):
            self.mat[i] = []
        if Edges:
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

    def Search_BFS(self, x):
    #     找到和x连通的所有点
        marked = [False for _ in range(self.V)]
        check_stack = [self.mat[x]]
        res = []
        while(check_stack):
            check_this = check_stack.pop(0)
            this_point = check_this[0].start
            if marked[this_point] == False:
                marked[this_point] = True
                res.append(this_point)
            for each in check_this:
                if marked[each.end] == False:
                    check_stack.append(self.mat[each.end])
        return res


    def LazyPrimMST(self):
        # 首先确认G是连通的
        if len(self.Search_BFS(0)) != self.V:
            raise ValueError("it is not a connected graph")

        marker = [False for _ in range(self.V)]
        mst = []

        MinPQ = []
#       MinPQ是核心，储存边
        marker[0] = True
        MinPQ += self.mat[0]
        MinPQ.sort(reverse=False)
        # print(MinPQ)
        while(MinPQ):
            edge_min = MinPQ.pop(0)
            start = edge_min.start
            end = edge_min.end
            if (marker[start] and marker[end]):
                continue
            else:
                mst.append(edge_min)
                if not marker[start]:
                    MinPQ += self.mat[start]
                    marker[start] = True
                if not marker[end]:
                    MinPQ += self.mat[end]
                    marker[end] = True
                MinPQ.sort()
        return mst

    def LazyPrimMST_weight(self):
        # 首先确认G是连通的
        if len(self.Search_BFS(0)) != self.V:
            raise ValueError("it is not a connected graph")

        marker = [False for _ in range(self.V)]
        mst = []

        MinPQ = []
        #       MinPQ是核心，储存边
        marker[0] = True
        MinPQ += self.mat[0]
        MinPQ.sort(reverse=False)
        # print(MinPQ)
        while (MinPQ):
            edge_min = MinPQ.pop(0)
            start = edge_min.start
            end = edge_min.end
            if (marker[start] and marker[end]):
                continue
            else:
                mst.append(edge_min)
                if not marker[start]:
                    MinPQ += self.mat[start]
                    marker[start] = True
                if not marker[end]:
                    MinPQ += self.mat[end]
                    marker[end] = True
                MinPQ.sort()
        res = 0
        for each in mst:
            res += each.weight
        return res


    def PrimMST(self):
#         marker and mst is replaced by edgeTo and distTo
        if len(self.Search_BFS(0)) != self.V:
            raise ValueError("it is not a connected graph")

        marker = [False for _ in range(self.V)]
        distTo = [float('inf') for _ in range(self.V)]
        pq = []
        mst = [None for _ in range(self.V)]
        # pq:优先队列
        distTo[0] = 0
        marker[0] = True
        for each in self.mat[0]:
            pq.append(each)
        pq.sort(reverse=False)

        while(pq):
            check_edge = pq.pop(0)
            marker[check_edge.end] = True

            if distTo[check_edge.end] > check_edge.weight:
                distTo[check_edge.end] = check_edge.weight
                mst[check_edge.end] = check_edge

            for each in self.mat[check_edge.end]:
                if marker[each.end] == False:
                    pq.append(each)
            pq.sort()
        print(sum(distTo))
        print(mst)
        return mst

    def PrimMST_weight(self):
#         最小生成树
#         marker and mst is replaced by edgeTo and distTo
        if len(self.Search_BFS(0)) != self.V:
            raise ValueError("it is not a connected graph")

        marker = [False for _ in range(self.V)]
        distTo = [float('inf') for _ in range(self.V)]
        pq = []
        mst = [None for _ in range(self.V)]
        # pq:优先队列
        distTo[0] = 0
        marker[0] = True
        for each in self.mat[0]:
            pq.append(each)
        pq.sort(reverse=False)

        while(pq):
            check_edge = pq.pop(0)
            marker[check_edge.end] = True
            if distTo[check_edge.end] > check_edge.weight:
                distTo[check_edge.end] = check_edge.weight
                mst[check_edge.end] = check_edge

            for each in self.mat[check_edge.end]:
                if marker[each.end] == False:
                    pq.append(each)
            pq.sort()

        return sum(distTo)


    def KruskalMST(self):
        def connect(x, y, Edges):
            tem_mat = {}
            for i in range(self.V):
                tem_mat[i] = []
            for each_Edge in Edges:
                tem_mat[each_Edge.start].append(each_Edge)
                tem_mat[each_Edge.end].append(each_Edge)

            res_list = [-1 for _ in range(self.V)]
            count = 1
            for i in range(len(res_list)):
                if res_list[i] == -1:
                    tem_stack = tem_mat[i]
                    while(tem_stack):
                        check_this_Edge = tem_stack.pop(0)
                        if res_list[check_this_Edge.start] == False:
                            res_list[check_this_Edge.start] = True
                            tem_stack += tem_mat[check_this_Edge.start]
                        if res_list[check_this_Edge.end] == False:
                            res_list[check_this_Edge.end] = True
                            tem_stack += tem_mat[check_this_Edge.end]
                    count += 1
            if res_list[x] == -1 or res_list[y] == -1:
                return False
            else:
                return res_list[x] == res_list[y]


        mst = []
        pq = []
        marker = [False for _ in range(self.V)]

        for i in range(self.V):
            for each in self.mat[i]:
                pq.append(each)
        pq.sort()

        while(pq and len(mst)<self.V-1):
            check_edge = pq.pop(0)
            if connect(check_edge.start, check_edge.end,mst):
                continue
            else:
                mst.append(check_edge)
                marker[check_edge.start] = True
                marker[check_edge.end] = True
        return mst




if __name__ == "__main__":

    Edges = [[4, 5, 0.35], [4, 7, 0.37], [5,7,0.28],[0,7,0.16],[1,5,0.32],[0,4,0.38],[2,3,0.17],[1,7,0.19],[0,2,0.26],[1,2,0.36],[1,3,0.29],[2,7,0.34],
             [6,2,0.4],[3,6,0.52],[6,0,0.58],[6,4,0.93]]
    G = EdgeWeightedGraph(8, Edges)
    print(G.mat)
    print(G.E)
    print(G.adj(0))
    print(G.Search_BFS(0))
    print(G.LazyPrimMST())
    print(G.LazyPrimMST_weight())
    print(G.PrimMST())
    print(G.PrimMST_weight())
    print(G.KruskalMST())
