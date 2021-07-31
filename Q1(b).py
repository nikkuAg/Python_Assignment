n = int(input())
coins = sorted(map(int, input().split()))
s = c =0
while sum(coins)>=s:
    s += coins.pop()
    c +=1
print(c)


