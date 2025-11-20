t = int(input())
ans_list = []
for _ in range(t):
    ans = 0
    n, k = map(int, input().split())
    k += 1
    a = list(map(int, input().split()))
    a_good_bad_num = [1]
    for i in range(1, n):
        if a[i] * 2 <= a[i - 1]:
            a_good_bad_num.append(0)
        else:
            a_good_bad_num.append(1)
    sum_of_bad_on_k = 0
    for i in range(1, k):
        if a_good_bad_num[i] == 0:
            sum_of_bad_on_k += 1
    if sum_of_bad_on_k == 0:
        ans += 1
    for i in range(k, n):
        if a_good_bad_num[i] == 0:
            sum_of_bad_on_k += 1
        if a_good_bad_num[i - (k - 1)] == 0:
            sum_of_bad_on_k -= 1
        if sum_of_bad_on_k == 0:
            ans += 1
    ans_list.append(ans)

for elem in ans_list:
    print(elem)