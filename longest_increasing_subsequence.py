from bisect import bisect_left
def longest_increasing_subsequence(x):
    n = len(x)
    p = [None] * n
    h = [None]
    # b：长度为k的序列的最长序列的最后一个元素，当x[i]大于b中所有的时候，就用x[i]令b增长
    b = [float('-inf')]

    for i in range(n):
        if  x[i] > b[-1]:
            p[i] = h[-1]
            h.append(i)
            b.append(x[i])
        else:
            # 二分查找到b[k-1] < x[i] <= b[k]
            k =bisect_left(b, x[i])
            print("k", k)
            h[k] = i
            b[k] = x[i]
            p[i] = h[k-1]

        print(b)
        print(p)
        print(h)

    q = h[-1]
    s = []

    while q is not None:
        s.append(x[q])
        q = p[q]

    return s[::-1]

print(longest_increasing_subsequence([4,5,7,1,2,3,4]))