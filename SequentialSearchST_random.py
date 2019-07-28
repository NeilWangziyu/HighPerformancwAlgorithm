# based on algorithm 3.1
class Node():
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next
    def __repr__(self):
        return "{}-{}".format(self.key, self.val)


class SequentialSearchST():
    def __init__(self, first_key, first_val):
        self.node_first = Node(key=first_key, val=first_val)

    def get(self, key):
        x = self.node_first
        while(x!=None):
            if x.key == key:
                return x.val
            x = x.next
        return None


    def put(self, key, val):
        # update exist val
        x = self.node_first
        while(x!=None):
            if x.key == key:
                x.val = val
                return
            x = x.next
        self.node_first = Node(key, val, self.node_first)
        return


    def size(self):
        pass


    def delete(self):
        pass







    def print(self):
        x = self.node_first
        while (x != None):
            print(x)
            x = x.next
        return



if __name__ == "__main__":
    ST = SequentialSearchST("S", 0)
    ST.put("E", 1)
    ST.put("A", 2)
    ST.put('R', 3)
    ST.put('C', 4)
    ST.put('H', 5)
    ST.put('E', 6)


    print(ST.get("S"))
    ST.print()