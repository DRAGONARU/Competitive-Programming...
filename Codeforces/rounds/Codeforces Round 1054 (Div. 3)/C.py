t = int(input())
ans = []
for i in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    b_list_of_counts = [0] * (n + 1)
    steps = 0
    for j in range(n):
        b_list_of_counts[a[j]] += 1
    for j in range(k):
        if b_list_of_counts[j] == 0:
            if b_list_of_counts[k] != 0:
                b_list_of_counts[k] -= 1
                steps += 1
            else:
                steps += 1
    ans.append(steps + b_list_of_counts[k])
for i in ans:
    print(i)
