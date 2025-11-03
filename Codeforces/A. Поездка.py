t = int(input())
ans = []
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    mx = a[0]
    for i in range(n - 1):
        mx = max(mx, a[i + 1] - a[i])
    ans.append(max(mx, 2 * (x - a[-1])))

for i in ans:
    print(i)
