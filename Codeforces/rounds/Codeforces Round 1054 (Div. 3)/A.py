t = int(input())
ans = []
for i in range(t):
    n = int(input())
    minus_1_count = 0
    zero_count = 0
    poisitive_count = 0
    a = list(map(int,input().split()))
    for j in range(n):
        if a[j] == -1:
            minus_1_count += 1
        elif a[j] == 0:
            zero_count += 1
        else:
            poisitive_count += 1
    ans.append(zero_count + (minus_1_count % 2) * 2)
for i in range(t):
    print(ans[i])
