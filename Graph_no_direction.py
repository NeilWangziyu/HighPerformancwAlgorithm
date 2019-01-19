class Graph():
    def __init__(self, V, Edges=None):
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


    def hasEdge(self, v, s):
        if v not in self.mat or s not in self.mat:
            raise ValueError("v or s not in this graph")
        if v in self.mat[s]:
            return True
        else:
            return False


    def addEdge(self, x, y):
        # 增加一条边，x-y
        if x not in self.mat or y not in self.mat:
            raise ValueError("x or y not in this graph")

        else:
            if y not in self.mat[x]:
                self.mat[x].insert(0, y)
            if x not in self.mat[y]:
                self.mat[y].insert(0, x)
            self.E += 1


    def delEdge(self, x, y):
        if x not in self.mat or y not in self.mat:
            raise ValueError("x or y not in this graph")
        else:
            self.mat[x].pop(self.mat[x].index(y))
            self.mat[y].pop(self.mat[y].index(x))
            self.E -= 1


    def addV(self, name):
        if name in self.mat:
            raise ValueError("the point is alrady exist")
        else:
            self.mat[name] = []
            self.V += 1


    def check_edge(self, x, y):
        """
        check if x-y exist
        """
        if x not in self.mat or y not in self.mat:
            raise ValueError("x or y not in this graph")
        else:
            if x in self.mat[y] and y in self.mat[x]:
                return True
            elif x not in self.mat[y] and y not in self.mat[x]:
                return False
            else:
                raise FileExistsError("this edge has problem")




    def search_BFS(self, x):
#         找到和x联通的所有点
        if x not in self.mat:
            raise ValueError("x not in this graph")

        check_list = [False for  _ in range(self.V)]
        check_list[x] = True
        check_stack = [self.mat[x]]
        while(check_stack):
            this_check = check_stack.pop(0)
            for each in this_check:
                if check_list[each] == False:
                    check_list[each] = True
                    check_stack.append(self.mat[each])
        res = []
        for i in range(self.V):
            if check_list[i] == True and i != x:
                res.append(i)
        return res

    def search_DFS(self, x):
        if x not in self.mat:
            raise ValueError("x not in this graph")

        check_list = [False for _ in range(self.V)]

        def DFS(index):
            if check_list[index] == False:
                check_list[index] = True
                for each in self.mat[index]:
                    DFS(each)
        DFS(x)

        res = []
        for i in range(self.V):
            if check_list[i] == True and i != x:
                res.append(i)
        return res

    def marked(self, x, y):
#         判断x和y是否联通
        if x not in self.mat or y not in self.mat:
            raise ValueError("x or y not in this graph")
        x_list_set = self.search_DFS(x)
        return y in x_list_set


    def count(self, x):
#         与定点x联通的所有点
        if x not in self.mat:
            raise ValueError("x or y not in this graph")
        v_list = self.search_BFS(x)
        return len(v_list)


    def Paths_DFS(self, s):
        """
        起点为s的所有路径
        DFS
        """
        if s not in self.mat:
            raise ValueError("s not in this graph")

        check_list = [False for _ in range(self.V)]
        res = []

        def DFS(x, list_tem):
            if check_list[x] == False:
                check_list[x] = True
                for each in self.mat[x]:
                    DFS(each, list_tem+[str(x)])
                if x != s:
                    res.append(list_tem+[str(x)])

        DFS(s, [])
        res_str = []
        for each in res:
            tem = each[0]+"-"+each[-1]+":"
            tem += "-".join(each)
            res_str.append(tem)
        return res_str


    def Paths_BFS(self, s):
        """
        BFS
        """
        if s not in self.mat:
            raise ValueError("s not in this graph")

        check_list = [False for _ in range(self.V)]
        res = []

        check_stack = [[s]]
        while check_stack:
            check_this = check_stack.pop(0)
            if check_list[check_this[-1]] == False:
                check_list[check_this[-1]] = True
                if check_this[-1] != s:
                    res.append(check_this)
                for each in self.mat[check_this[-1]]:
                    check_stack.append(check_this+[each])
        # print(res)
        res_str = []
        for each in res:
            each = list(map(str, each))
            tem = str(each[0]) + "-" + str(each[-1]) + ":"
            tem += "-".join(each)
            res_str.append(tem)
        return res_str


    def hasPathTo(self, s, v):
        """
        是否存在s-v的路径
        """
        if s not in self.mat or v not in self.mat:
            raise ValueError("s or v not in this graph")

        check_list = [False for _ in range(self.V)]
        res = []

        check_stack = [[s]]
        while check_stack:
            check_this = check_stack.pop(0)
            if check_list[check_this[-1]] == False:
                check_list[check_this[-1]] = True
                if check_this[-1] != s:
                    res.append(check_this)
                for each in self.mat[check_this[-1]]:
                    check_stack.append(check_this+[each])
        # print(res)
        for each in res:
            if each[0] == s and each[-1] == v:
                return True
        return False



    def Pathto(self, s, v):
        """
        给出路径或者 None
        :return:
        """
        if s not in self.mat or v not in self.mat:
            raise ValueError("s or v not in this graph")

        check_list = [False for _ in range(self.V)]
        res = []

        check_stack = [[s]]
        while check_stack:
            check_this = check_stack.pop(0)
            if check_list[check_this[-1]] == False:
                check_list[check_this[-1]] = True
                if check_this[-1] != s:
                    res.append(check_this)
                for each in self.mat[check_this[-1]]:
                    check_stack.append(check_this+[each])

        # print(res)
        for each in res:
            if each[0] == s and each[-1] == v:
                each = list(map(str, each))
                tem = str(each[0]) + "-" + str(each[-1]) + ":"
                tem += "-".join(each)
                return tem
        return None


    def DegreeOfSeparation(self, s, v):
        """
        返回s和v之间的间隔
        """
        if s not in self.mat or v not in self.mat:
            raise ValueError("s or v not in this graph")

        check_list = [False for _ in range(self.V)]
        res = []

        check_stack = [[s]]
        while check_stack:
            check_this = check_stack.pop(0)
            if check_list[check_this[-1]] == False:
                check_list[check_this[-1]] = True
                if check_this[-1] != s:
                    res.append(check_this)
                for each in self.mat[check_this[-1]]:
                    check_stack.append(check_this + [each])

        # print(res)
        for each in res:
            if each[0] == s and each[-1] == v:
                return len(each)-2
        return -1



    def CC(self):
        """
        联通分量，返回一个list，每个值代表这个定点属于哪个联通分量，使用DFS
        :return:
        """
        def DFS(index):
            if res_list[index] == -1:
                res_list[index] = count
                check = self.mat[index]
                for each in check:
                    DFS(each)

        res_list = [-1 for _ in range(self.V)]
        count = 1
        for i in range(len(res_list)):
            if res_list[i] == -1:
                DFS(i)
                count += 1

        return res_list

    def connected(self, v, w):
        """
        判断v和w是否相连
        """
        if w not in self.mat or v not in self.mat:
            raise ValueError("w or v not in this graph")

        marked = self.CC()
        return marked[v] == marked[w]


    def id(self, v):
        """
        v联通分量的标识符
        """
        if v not in self.mat:
            raise ValueError("v not in this graph")
        marked = self.CC()
        return marked[v]





    def __len__(self):
        return self.V




if __name__ == "__main__":
    Edges = [[0, 5], [4,3], [0, 1], [9, 12], [6, 4], [5, 4], [0, 2], [11,12], [9, 10], [0, 6], [7, 8], [9, 11], [5, 3]]
    G = Graph(14, Edges=Edges)
    print(G.mat)
    # G.delEdge(0,5)
    # print(G.mat)
    # print(G.check_edge(4, 3))
    # print(G.check_edge(5, 9))
    # print(G.search_BFS(0))
    # print(G.search_BFS(12))
    # print(G.marked(0, 12))
    # print(G.search_DFS(0))
    # print(G.search_DFS(12))
    # print(G.marked(0, 12))
    # print(G.count(5))
    print(G.Paths_DFS(0))
    print(G.Paths_BFS(0))
    print(G.hasPathTo(6, 7))
    print(G.Pathto(8, 7))
    print(G.Paths_BFS(12))
    print(G.Pathto(12, 10))
    print(G.CC())
    print(G.connected(0,13))
    print(G.connected(0,5))
    print(G.DegreeOfSeparation(0, 4))









