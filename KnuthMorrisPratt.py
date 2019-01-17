s = "ADEADBCABABCABCDABDADBEA"
t = "ABCDABD"

def KMP(s, t):
    len_s = len(s)
    len_t = len(t)
    r = [0] * len_t
    r[0] = -1
    j = -1
    print(r)

    for i in range(1, len_t):
        while j >= 0 and t[i-1] != t[j]:
            j = r[j]
        j += 1
        r[i] = j
    # 用r[j]来记录j减去自身与t[0,...,j-1]的差值

    j = 0
    print(r)

    for i in range(len_s):
        while j >= 0 and s[i] !=t[j]:
            j = r[j]
        j += 1
        if j == len_t:
            return i - len_t + 1
    return -1

print(KMP(s, t))