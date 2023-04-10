def array_intersection(a1, a2):
    x1,x2 = len(a1),len(a2)
    A,count = [],0

    if x1>=x2:
        for i in a2:
            if i in a1:
                A.append(i)
                a1.remove(i)
                count += 1

    else:
        for i in a1:
            if i in a2:
                A.append(i)
                a2.remove(i)
                count += 1

    
    if count==0:
        return [count]

    else:
        return [count,"\n"]+A

n, m = map(int, input().split(' '))
a1 = list(map(int, input().split(' ')))
a2 = list(map(int, input().split(' ')))
intersection = array_intersection(a1, a2)
print(' '.join(map(str, intersection)))
