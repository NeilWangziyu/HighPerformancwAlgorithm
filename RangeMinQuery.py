class RangeMinQuery:
    def __init__(self, t, INF=float('inf')):
        self.INF = INF
        self.N = 1
        while self.N < len(t):
            self.N *= 2

        self.s = [self.INF] * 2 * self.N

        for i in range(len(t)):
            self.s[self.N + i] = t[i]
        for p in range(self.N -1 , 0, -1):
            self.s[p] = min(self.s[2*p], self.s[2*p+1])
        print(self.s)

    def __getitem__(self, i):
        return self.s[self.N + i]

    def __setitem__(self, i, v):
        p = self.N + i
        self.s[p] = v
        p //= 2
        while p > 0:
            self.s[p] = min(self.s[2*p], self.s[2*p + 1])
            p //= 2
        print(self.s)


    def range_min(self, i, k):
        return self._range_min(1, 0, self.N, i, k)

    def _range_min(self, p, start, span, i, k):
        if start + span <= i or k <= start:
            return self.INF
        if i <= start and start + span <=k:
            return self.s[p]

        left = self._range_min(2*p, start, span//2, i, k)
        right = self._range_min(2*p+1, start+span//2, span//2, i, k)
        return min(left, right)





s = RangeMinQuery([3,1,9,8,3,4,2,7,5])
print(s[4])
s[4] = 10

print(s.range_min(0,4))
s[0] = 0
print(s.range_min(0,4))