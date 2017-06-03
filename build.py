import operator


def solution_asc(dic):
    return sorted(x.items(), key=operator.itemgetter(0))


def solution_desc(dic):
    return sorted(x.items(), key=operator.itemgetter(0), reverse=True)

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print solution_asc(x)
print solution_desc(x)
