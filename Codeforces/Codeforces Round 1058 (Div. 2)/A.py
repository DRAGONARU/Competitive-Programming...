t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(101):
        if i not in a:
            ans.append(i)
            break
for i in ans:
    print(i)
