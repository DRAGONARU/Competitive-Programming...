t = int(input())
ans = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    i = n - 1
    ans_t = 0
    while i >= 0:
        if s[i] == '1':
            if '1' not in s[max(i - k + 1, 0) : i]:
                ans_t += 1
        i -= 1
    ans.append(ans_t)
for i in ans:
    print(i)
