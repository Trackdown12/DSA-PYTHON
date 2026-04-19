def duplicate(l:list)->bool:
    a=False
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                a=True
    return a
l=[12,2,1,2,1,3,2,1,4,12]
print(duplicate(l))