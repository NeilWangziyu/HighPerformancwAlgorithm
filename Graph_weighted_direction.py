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

class PrioQue_point():
    def __init__(self, num, val):
        self.num = num
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

    def __repr__(self):
        return "{}:{}".format(self.num, self.val)



class EdgeWeightedBiGraph():
    def __init__(self, V, Edges):
        self.V = V
        self.E = 0
        self.mat = {}
        for i in range(self.V):
            self.mat[i] = []
        if Edges:
            for each in Edges:
                self.addEdge(each[0], each[1], each[2])


    def addEdge(self, start, end , weight):
        if start and end not in self.mat:
            raise ValueError("wrong edge")
        self.mat[start].insert(0, weightedEdge(start, end , weight))
        self.E += 1


    def adj(self, v):
        if v not in self.mat:
            raise ValueError("wrong v")
        return self.mat[v]


    def DijkstraSP(self, v):
        # 需要PQ这个优先队列
        def check_in_pq(num, pq):
            for index, each in enumerate(pq):
                if each.num == num:
                    return index
            return False

        def relax(p):
            # p is the check point
            for each_Edge in self.adj(p):
                w = each_Edge.end
                if distTo[w] > distTo[p] + each_Edge.end:
                    distTo[w] = distTo[p] + each_Edge.weight
                    edgeTo[w] =each_Edge
                    if check_in_pq(w, pq):
                        index = check_in_pq(w, pq)
                        pq[index].val = distTo[w]
                    else:
                        pq.append(PrioQue_point(w, distTo[w]))

        if v not in self.mat:
            raise ValueError("wrong v")

        edgeTo = [[] for _ in range(self.V)]
        distTo = [float('inf') for _ in range(self.V)]
        # pq里面是定点
        pq = []

        # init
        # pq with point
        distTo[0] = 0
        pq.append(PrioQue_point(0, 0))

        while(pq):
            check_point = pq.pop(0).num
            relax(check_point)
            pq.sort(reverse=False)
            # print(pq)

        # print(edgeTo)
        # print(distTo)
        return edgeTo, distTo




    def DistTo(self, s, v):
        """
        the smallest weight from s to v
        """
        if v not in self.mat:
            raise ValueError("wrong v")
        edgeTo, distTo = self.DijkstraSP(s)
        return distTo[v]



    def hasPathTo(self , s, v):
        """
        if there is s to v
        """
        if v not in self.mat:
            raise ValueError("wrong v")
        edgeTo, distTo = self.DijkstraSP(s)
        return not distTo[v]==float('inf')


    def PathTo(self, s, v):
        """
        return the edges from s to v
        """
        if v not in self.mat:
            raise ValueError("wrong v")

        edgeTo, distTo = self.DijkstraSP(s)
        if distTo[v]==float('inf'):
            return "no path"

        path = []
        e = edgeTo[v]
        while(e):
            path.append(e)
            e = edgeTo[e.start]
        path.reverse()
        return path

    def DirectedCycle(self):
        # 寻找cycle
        def DFS_cycle(index):
            marked[index] = True
            OnStack[index] = True
            for each_edge in self.adj(index):
                each = each_edge.end
                if OnStack[each]:
        #             find cycle
                    tem_cycle = []
                    x = index
                    while(x != each):
                        tem_cycle.append(x)
                        x = edgeTo[x]
                    tem_cycle.append(each)
                    tem_cycle.append(index)
                    Cycle.append(tem_cycle)
                else:
        #             继续寻找
                    edgeTo[each] = index
                    DFS_cycle(each)
            OnStack[index] = False


        marked = [False for _ in range(self.V)]
        OnStack = [False for _ in range(self.V)]
        edgeTo = [-1 for _ in range(self.V)]
        Cycle = []
        for i in range(self.V):
            if not marked[i]:
                DFS_cycle(i)
        return Cycle

    def hasCycle(self):
        "True: have cycle"
        return len(self.DirectedCycle()) != 0


    def DepthFirstOrder(self):
        #返回顶点排序
        #利用DFS
        pre = []                #queue
        post = []               #queue
        reversePost = []        #stack
        marked = [False for _ in range(self.V)]

        def DFS_firstOrder(v):
            pre.append(v)
            marked[v] = True
            for each_edge in self.adj(v):
                w = each_edge.end
                if marked[w] == False:
                    DFS_firstOrder(w)
            post.append(v)
            reversePost.insert(0, v)

        for index in range(self.V):
            if marked[index] == False:
                DFS_firstOrder(index)

        return pre, post, reversePost

    def Topological(self):
        # 返回顶点排序
        # 利用DFS
        if self.hasCycle():
            raise ValueError("only in no cycle graph")

        reversePost = []  # stack
        marked = [False for _ in range(self.V)]

        def DFS_firstOrder(v):
            marked[v] = True
            for each_edge in self.adj(v):
                w = each_edge.end
                if marked[w] == False:
                    DFS_firstOrder(w)
            reversePost.insert(0, v)

        for index in range(self.V):
            if marked[index] == False:
                DFS_firstOrder(index)

        return reversePost


    def AcylicSP(self, s):
    #   无环加权有向图最短路径算法
    #   生成最短路径树
    #   s:start
        def relax(index):
            for each_next_edge in self.adj(index):
                end_point = each_next_edge.end
                if distTo[end_point] > distTo[index] + each_next_edge.weight:
                    distTo[end_point] = distTo[index] + each_next_edge.weight
                    edgeTo[end_point] = each_next_edge

        if self.hasCycle():
            raise ValueError("only in no cycle graph")


        edgeTo = [None for _ in range(self.V)]
        distTo = [float('inf')for _ in range(self.V)]
        distTo[s] = 0
        top = self.Topological()

        for each in top:
            # each is the points
            relax(each)
        return edgeTo, distTo


    def PathTo_no_cycle(self, s, v):
        """
        无环加权有向图最短路径算法,返回s - v最短路径
        return the edges from s to v
        """
        if v not in self.mat or s not in self.mat:
            raise ValueError("wrong v or s")

        if self.hasCycle():
            raise ValueError("the graph shoud be no cycle")

        edgeTo, distTo = self.AcylicSP(s)
        if distTo[v] == float('inf'):
            return "no path"

        path = []
        e = edgeTo[v]
        while (e):
            path.append(e)
            e = edgeTo[e.start]
        path.reverse()
        return path

    def AcylicSP_longest(self, s):
    #         无环加权有向图最长路径算法
    #           生成最长路径树
    #          s:start
        def relax(index):
            for each_next_edge in self.adj(index):
                end_point = each_next_edge.end
                if distTo[end_point] < distTo[index] + each_next_edge.weight:
                    distTo[end_point] = distTo[index] + each_next_edge.weight
                    edgeTo[end_point] = each_next_edge

        if self.hasCycle():
            raise ValueError("only in no cycle graph")


        edgeTo = [None for _ in range(self.V)]
        distTo = [-float('inf')for _ in range(self.V)]
        distTo[s] = 0
        top = self.Topological()

        for each in top:
            # each is the points
            relax(each)
        return edgeTo, distTo



if __name__ == "__main__":
    Edges_cycle = [[4,5,0.35],[5,4,0.35],[4,7,0.37],[5,7,0.28],[7,5,0.28],[5,1,0.32],[0,4,0.38],[0,2,0.26],[7,3,0.39],[1,3,0.29],[2,7,0.34],[6,2,0.4],[3,6,0.52],
             [6,0,0.58],[6,4,0.93]]
    G = EdgeWeightedBiGraph(8, Edges_cycle)
    print(G.mat)
    # print(G.hasPathTo(0, 3))
    # print(G.DistTo(0,3))
    # print(G.PathTo(0, 3))
    for i in range(1, G.V):
        print(G.PathTo(0, i))
    # print(G.DirectedCycle())
    # print(G.DepthFirstOrder())
        
    Edges_no_cycle = [[5,4,0.35],[4,7,0.37],[5,7,0.28],[5,1,0.32],[4,0,0.38],[0,2,0.26],[3,7,0.39],[1,3,0.29],[7,2,0.34],[6,2,0.4],[3,6,0.52],
             [6,0,0.58],[6,4,0.93]]

    G_no_cyc = EdgeWeightedBiGraph(8, Edges_no_cycle)
    print(G_no_cyc.mat)
    print(G.E)
    # print(G_no_cyc.DepthFirstOrder())
    print(G_no_cyc.Topological())
    print(G_no_cyc.AcylicSP(5))
    for i in range(G_no_cyc.V):
        print(G_no_cyc.PathTo_no_cycle(5, i))
    print(G_no_cyc.AcylicSP_longest(5))


    # -----
    # 关键路径问题]
    print("关键路径问题")
    E_key_route = [[0, 1, 41], [0, 7, 41],  [0, 9, 41],  [1, 2, 51], [6, 8, 21], [6, 3, 21], [7, 3, 32], [7,8, 32], [8, 2, 32], [9, 4, 29],
                   [9, 6, 29]]
    G_key_route = EdgeWeightedBiGraph(10, E_key_route)
    print(G_key_route.mat)

    print(G_key_route.AcylicSP_longest(0))



