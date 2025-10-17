class bracket_num:
    def __init__(self, num, bracket):
        self.num = num
        self.bracket = bracket

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    c = list(map(int,input().split()))
    c = sorted(c)
    steck = []
    for i in range(n * 2):
        if i < n:
            steck.append(bracket_num(l[i], '('))
        else:
            steck.append(bracket_num(r[i - n], ')'))
    steck.sort(key=lambda x: x.num)
    stack2 = []
    l_of_su = []
    su = 0
    for i in range(n * 2 - 1, -1, -1):
        if steck[i].bracket == '(':
            l_of_su.append(stack2[-1].num - steck[i].num)
            stack2.pop()
        else:
            stack2.append(steck[i])
    l_of_su.sort(reverse=True)
    for i in range(n):
        su += c[i] * l_of_su[i]
    ans.append(su)
for i in ans:
    print(i)
