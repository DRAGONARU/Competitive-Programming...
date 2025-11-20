s = input().replace('ovo', 'oo')
s_converted = []
converted_count = 0
sum_total = 0
ans = 0
for i in range(len(s) - 1):
    if s[i] == 'v' and s[i + 1] == 'v':
        converted_count += 1
    elif s[i] == 'o':
        sum_total += converted_count
        s_converted.append(converted_count)
        converted_count = 0
        s_converted.append('o')
s_converted.append(converted_count)
sum_total += converted_count
sum_left = 0
for elem in s_converted:
    if elem != 'o':
        sum_left += elem
        sum_total -= elem
    else:
        ans += sum_left * sum_total
print(ans)