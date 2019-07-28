class Digraph():
    def __init__(self, V,Edges=None):
        # V：顶的个数
        # E: 边的条数
        # 利用数字来表示定点
        self.V = V
        self.mat = {}
        self.E = 0
        for i in range(V):
            self.mat[i] = []

        if Edges:
            for each in Edges:
                self.addEdge(each[0], each[1])



    def addEdge(self, v, w):
        # from v to w
        if v not in self.mat or w not in self.mat:
            raise ValueError("not in graph")

        if w not in self.mat[v]:
            self.mat[v].insert(0, w)
            self.E += 1



    def adj(self, v):
        if v not in self.mat:
            raise ValueError("v not in graph")
        return self.mat[v]


    def reverse(self):
        DiGraph_R = Digraph(self.V)
        for i in range(self.V):
            for each_edge in self.adj(i):
                DiGraph_R.addEdge(each_edge, i)
        return DiGraph_R


    def DirectedDFS(self, s):
#         从Graph中找到所有s出发可达的定点
        if s not in self.mat:
            raise ValueError("s not in graph")
        res = []
        check = [False for _ in range(self.V)]

        def DFS(index):
            if check[index] == False:
                check[index] = True
                if index != s:
                    res.append(index)
                for each in self.mat[index]:
                    DFS(each)
        DFS(s)
        return res


    def DirectedBFS(self, s):
        if s not in self.mat:
            raise ValueError("s not in graph")
        res = []
        check = [False for _ in range(self.V)]
        check_stack = [s]
        while(check_stack):
            this = check_stack.pop(0)
            if check[this] == False:
                check[this] = True
                if this != s:
                    res.append(this)
                for each in self.mat[this]:
                    check_stack.append(each)
        return res


    def DirectedMarked(self,s, v):
#         is v reached able from s
        if v not in self.mat or s not in self.mat:
            raise ValueError("not in graph")
        s_reachable = self.DirectedDFS(s)
        return v in s_reachable



    def DirectedCycle(self):
#         利用DFS, return all cycles
        def DFS_circle(index):
            onStack[index] = True
            marked[index] = True
            # print(index, onStack, marked)
            for w in self.adj(index):
                if onStack[w]:
                    # print("find cycle")
                    res_Tem = []
                    x = index
                    while(x!=w):
                        res_Tem.append(x)
                        x = edgeTo[x]
                    res_Tem.append(w)
                    res_Tem.append(index)
                    cycle.append(res_Tem)
                else:
                    edgeTo[w] = index
                    DFS_circle(w)
            onStack[index] = False


        marked = [False for _ in range(self.V)]
        edgeTo = [-1 for _ in range(self.V)]
        cycle = []
        onStack = [False for _ in range(self.V)]
        for i in range(self.V):
            if marked[i] == False:
                DFS_circle(i)
        # print(cycle)
        return cycle


    def hasCycle(self):
        "True: have cycle"
        return len(self.DirectedCycle()) != 0


    def DepthFirstOrder(self):
#         返回顶点排序
#         利用DFS
        pre = []                #queue
        post = []               #queue
        reversePost = []        #stack
        marked = [False for _ in range(self.V)]

        def DFS_DepthFirstOrder(v):
            pre.append(v)
            marked[v] = True
            for w in self.adj(v):
                if marked[w] == False:
                    DFS_DepthFirstOrder(w)
            post.append(v)
            reversePost.insert(0, v)


        for index in range(self.V):
            if marked[index] == False:
                DFS_DepthFirstOrder(index)

        # print(pre)
        # print(post)
        # print(reversePost)
        return pre, post, reversePost

    def pre(self):
        #         返回顶点排序
        #         利用DFS

        pre = []  # queue
        reversePost = []  # stack
        marked = [False for _ in range(self.V)]

        def DFS_DepthFirstOrder(v):
            pre.append(v)
            marked[v] = True
            for w in self.adj(v):
                if marked[w] == False:
                    DFS_DepthFirstOrder(w)
            reversePost.insert(0, v)

        for index in range(self.V):
            if marked[index] == False:
                DFS_DepthFirstOrder(index)
        return pre

    def post(self):
        #         返回顶点排序
        #         利用DFS

        post = []  # queue
        marked = [False for _ in range(self.V)]

        def DFS_DepthFirstOrder(v):
            marked[v] = True
            for w in self.adj(v):
                if marked[w] == False:
                    DFS_DepthFirstOrder(w)
            post.append(v)
        for index in range(self.V):
            if marked[index] == False:
                DFS_DepthFirstOrder(index)
        return post


    def reversePost(self):
        #         返回顶点排序
        #         利用DFS

        reversePost = []  # stack
        marked = [False for _ in range(self.V)]

        def DFS_DepthFirstOrder(v):
            marked[v] = True
            for w in self.adj(v):
                if marked[w] == False:
                    DFS_DepthFirstOrder(w)
            reversePost.insert(0, v)

        for index in range(self.V):
            if marked[index] == False:
                DFS_DepthFirstOrder(index)

        return reversePost

    def Topological(self):
        #         返回顶点排序的逆后序
        #         利用DFS
        if self.hasCycle() != 0:
            # 保证是无环图
            return None
        return self.reversePost()


    def KosarajuSCC(self):
#         强连通分量，先求逆图，再找到拓扑结构，再DFS
        def DFS_KosarajuSCC(i):
            marked[i] = True
            ID[i] = count
            for each in self.adj(i):
                if marked[each] == False:
                    DFS_KosarajuSCC(each)


        reverse_G = self.reverse()
        # print(reverse_G.mat)
        rever_order = reverse_G.reversePost()
        count = 1
        # print(rever_order)
        marked = [False for _ in range(self.V)]
        ID = [-1 for _ in range(self.V)]
        for each in rever_order:
            if marked[each] == False:
                DFS_KosarajuSCC(each)
                count += 1
        return ID


    def StronglyConnected(self, v, w):
        if v not in self.mat or w not in self.mat:
            raise ValueError("not in graph")
        ID_list = self.KosarajuSCC()
        return ID_list[v]==ID_list[w]

    def TransitiveClosure(self, v, w):
        # 能否从v到达w
        if v not in self.mat or w not in self.mat:
            raise ValueError("not in graph")

        return w in self.DirectedDFS(v)



if __name__ == "__main__":
    Edges = [[4,2], [2,3], [3,2], [6,0], [0, 1], [2,0],[11,12], [12,9], [9, 10], [9, 11], [8, 9], [10, 12], [11, 4],
             [4, 3], [3, 5], [7, 8], [8, 7], [5, 4], [0, 5], [6, 4], [6, 9], [7, 6]]
    # Edges = [[0,5], [3, 5], [5, 4], [4, 3], [9,10],[10,12],[12,9],[9,11],[11,12], [2, 3], [3,2], [2,0]]
    # Edges_no_cycle = [[0,1], [0,5], [2, 0], [2, 3], [3,5], [5,4],[0,6],[6,4],[7,6],[6,9],[8,7],[9,10],[9,12],[9,11],[11,12]]
    G = Digraph(13, Edges)
    print(G.mat)
    # print(G.E)
    # G_R = G.reverse()
    # print(G_R.mat)
    print(G.DirectedDFS(0))
    # print(G.DirectedBFS(0))
    print("cycle",G.DirectedCycle())
    print(G.hasCycle())
    # print(G.DepthFirstOrder())
    # print(G.pre())
    # print(G.post())
    # print(G.reversePost())
    # print(G.Topological())
    print(G.KosarajuSCC())
    print(G.StronglyConnected(0, 12))
    print(G.TransitiveClosure(6, 12))







