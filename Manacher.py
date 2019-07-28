def manacher(s):
    assert '$' not in s and '^' not in s and '#' not in s
    if s == "":
        return (0, 1)
    t = '^#' + '#'.join(s) +'#$'

    c = 0
    d = 0
    p = [0] * len(t)
    print(t)
    for i in range(1, len(t)-1):
        # 相对于中心c翻转i
        mirror = 2*c-i
        print(i, c, d)
        # 增加以i为中心的回文字串长度
        p[i] = max(0, min(d-i, p[mirror]))

        while t[i+1+p[i]] == t[i-1-p[i]]:
            p[i] += 1
        print(p[i])
        if i + p[i] > d:
            c = i
            d = i + p[i]
    print(p)
    (k, i) = max((p[i], i) for i in range(1, len(t)-1))
    print((k, i))
    return ((i - k)//2, (i+k)//2)


print(manacher("aaabaa"))

print(manacher("abcdedcbcded"))
