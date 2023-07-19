def findResult(n,string):
    a,b = ['1'],['1']
    flag = 0
    for i in range(1,n):
        if not flag:
            if string[i]=='2':
                a.append('1')
                b.append('1')
            elif string[i]=='1':
                a.append('1')
                b.append('0')
                flag = 1
            else:
                a.append('0')
                b.append('0')
        else:
            a.append('0')
            b.append(string[i])
    print(''.join(a))
    print(''.join(b))



T = int(input())
for _ in range(T):
    length = int(input())
    c = input()

    findResult(length,c)