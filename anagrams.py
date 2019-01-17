print("hello world")


def anagrams(W):
    check_list = list(set(W.split(' ')))
    dict = {}
    for each in check_list:
        tem = list(each)
        tem_str = "".join(sorted(tem))
        if tem_str not in dict:
            dict[tem_str] = [each]
        else:
            dict[tem_str].append(each)
    res = []
    for each in dict:
        if len(dict[each]) > 1:
            res.append(dict[each])

    return res



s = "le cgueb narche vers sa niche et trouve une limace de chine dog god six xis "
print(anagrams(s))