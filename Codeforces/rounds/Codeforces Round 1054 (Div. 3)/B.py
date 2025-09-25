t = int(input())
ans = []
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    mnmx = -(10 ** 9 + 1)
    for j in range(0, n-1, 2):
        ts = -a[j] + a[j+1]
        mnmx = max(mnmx, ts)
    ans.append(mnmx)
for i in ans:
    print(i)
