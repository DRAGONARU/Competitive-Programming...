t = int(input())
ans = []
for _ in range(t):
    a = int(input())
    sta = bin(a)[2:]
 
    f = True
    i_k = len(sta) - 1
    r_zeros = 0
    while sta[i_k] == '0' and i_k >= 0:
        r_zeros += 1
        i_k -= 1
    sta = r_zeros * '0' + sta
    left = 0
    right = len(sta) - 1
    center = (left + right) // 2
    if sta[center] == '1' and len(sta) % 2 == 1:
        f = False
    else:
        while left <= right and f:
            if sta[left] != sta[right]:
                f = False
            left += 1
            right -= 1
    ans.append('YES' if f else 'NO')
for i in ans:
    print(i)
