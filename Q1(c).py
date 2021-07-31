def find_index(mlist, item):
    for sub in mlist:
        if item in sub:
            return (mlist.index(sub), sub.index(item))

matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))

x = find_index(matrix, 1)[0]
y = find_index(matrix, 1)[1]

print (abs(x-2) + abs(y-2))