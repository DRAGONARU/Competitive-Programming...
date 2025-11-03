t = int(input())
ans = []
for _  in range(t):
    n, k = map(int, input().split())
    f = True
    a = list(map(int, input().split()))
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            f = False
    if not f and k == 1:
        ans.append("NO")
    else:
        ans.append("YES")
for i in ans:
    print(i)
