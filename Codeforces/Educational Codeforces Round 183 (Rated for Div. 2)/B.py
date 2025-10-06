
t = int(input())
ans = []
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    a = []
    left_killed = 0
    right_killed = 0
    unowen = 0
    for j in range(len(s)):
        if s[j] == '0':
            left_killed += 1
        elif s[j] == '1':
            right_killed += 1
        else:
            unowen += 1
    x_mi = left_killed
    x_mx = left_killed + unowen
    rl = n - k
    for i in range(1, n + 1):
        L_i = i - rl
        R_i = i - 1
        L = max(x_mi, L_i)
        R = min(x_mx, R_i)
        if L > R:
            a.append('-')
        else:
            if x_mi >= L_i and x_mx <= R_i:
                a.append('+')
            else:
                a.append('?')
    ans.append(''.join(a))
for i in ans:
    print(i)
