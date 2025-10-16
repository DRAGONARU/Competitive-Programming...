t = int(input())
ans = []
a = ''
hash = {'000' : '0', '001' : '1', '111' : '0', '110' : '1', '101' : '1', '010' : '1'}
for _ in range(t):
    a = ''
    f = True
    b, c, d = map(int, input().split())
    bin_b = bin(b)[2:]
    bin_c = bin(c)[2:]
    bin_d = bin(d)[2:]
    max_len = max(len(bin_b), len(bin_c), len(bin_d))
    if max_len != len(bin_b):
        bin_b = '0' * (max_len - len(bin_b)) + bin_b
    if max_len != len(bin_c):
        bin_c = '0' * (max_len - len(bin_c)) + bin_c
    if max_len != len(bin_d):
        bin_d = '0' * (max_len - len(bin_d)) + bin_d
    for i in range(len(bin_d)):
        if not f:
            break
        if bin_d[i] == '1' and bin_c[i] == '1' and bin_b[i] == '0':
            f = False
        elif bin_d[i] == '0' and bin_c[i] == '0' and bin_b[i] == '1':
            f = False
        else:
            a += hash[bin_b[i] + bin_c[i] + bin_d[i]]
    if f:
        ans.append(int(a, 2))
    else:
        ans.append(-1)
for i in ans:
    print(i)
