t = int(input())
ans = []
for i in range(t):
    n, k = map(int, input().split())
    if n * n - k == 1:
        ans.append(['NO', -1])
    else:
        k = n * n - k
        mtrx = [ [''] * n for _ in range(n)]
        for j in range(n):
            for l in range(n):
                if k != 1 and k != 0:
                    if l == 0:
                        k -= 1
                        mtrx[j][l] = 'R'
                    else:
                        k -= 1
                        mtrx[j][l] = 'L'
                elif l == 0 and k != 0:
                    k -= 1
                    mtrx[j][l] = 'U'
                elif k != 0:
                    k -= 1
                    mtrx[j][l] = 'L'
                else:
                    mtrx[j][l] = 'D'
        ans.append(['YES', mtrx])
for i in ans:
    if i[0] == 'YES':
        print(i[0])
        for j in i[1]:
            print(''.join(j))
    else:
        print(i[0])
