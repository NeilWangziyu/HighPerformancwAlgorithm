class BinarySearchST():
    def __init__(self):
        self.keys = []
        self.value = []
        self.N = 0

    def size(self):
        return self.N

    def rank(self, key):
        s = 0
        e = self.N - 1
        while(s <= e):
            mid = (s + e) // 2
            if self.keys[mid] == key:
                return mid
            elif self.keys[mid] < key:
                s = mid + 1
            else:
                e = mid - 1
        return s



    def get(self, key):
        if self.size()==0:
            return None
        index = self.rank(key)
        if index < self.N and self.keys[index]==key:
            return self.value[index]
        else:
            return None


    def put(self, key, val):
        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            self.value[i] = val
            return
        else:
            self.keys.insert(i, key)
            self.value.insert(i, val)
            self.N += 1

    def delete(self, key):
        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            self.value.pop(i)
            self.keys.pop(i)
            self.N -= 1
            return
        else:
            print("wrong in delete")
            return

    def __repr__(self):
        print(self.keys)
        print(self.value)
        return "finish"





if __name__ == "__main__":
    ST = BinarySearchST()
    ST.put("S", 0)

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

    print(ST)
    ST.delete('A')
    print(ST)
    ST.delete('A')
    print(ST)

