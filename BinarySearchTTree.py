class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.N = 1

    def __repr__(self):
        return "{}-{}".format(self.key, self.val)

class BinarySearchTree():
    def __init__(self,key, val):
        self.root = Node(key, val)

    def size(self):
        if self.root:
            return self.root.N
        else:
            return None

    def get(self, key):
        if not self.root:
            return "empty tree, None"

        tree_node = self.root
        while(tree_node):
            if tree_node.key == key:
                return tree_node
            else:
                if tree_node.key > key:
                    tree_node = tree_node.left
                else:
                    tree_node = tree_node.right
        return "None"


    def put(self, key, val):
        if not self.root:
            self.root = Node(key, val)
            return
        else:
            tree_node = self.root
            while (tree_node):
                if tree_node.key == key:
                    tree_node.val = val
                    return
                elif tree_node.key > key:
                    if tree_node.left:
                        tree_node = tree_node.left
                    else:
                        tree_node.left = Node(key, val)
                else:
                    if tree_node.right:
                        tree_node = tree_node.right
                    else:
                        tree_node.right = Node(key, val)

    def print(self):
        if not self.root:
            print('[]')
            return
        else:
            res = []
            tem_stack = [self.root]
            while(tem_stack):
                check = tem_stack.pop()
                res.append(check)
                if check.right:
                    tem_stack.append(check.right)
                if check.left:
                    tem_stack.append(check.left)
            print(res)




if __name__ == "__main__":
    ST = BinarySearchTree('S', 0)
    ST.put("E", 1)
    ST.put("A", 2)
    ST.put('R', 3)
    ST.put('C', 4)
    ST.put('H', 5)
    ST.put('E', 6)
    ST.put('X', 7)
    ST.put('A', 8)
    ST.put('M', 9)
    ST.put('P', 10)
    ST.put('L', 11)
    ST.put('E', 12)
    ST.print()
    print(ST.get('L'))


