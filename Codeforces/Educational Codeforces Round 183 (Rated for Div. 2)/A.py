
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ans.append((3 - n % 3) % 3)
for i in ans:
    print(i)
