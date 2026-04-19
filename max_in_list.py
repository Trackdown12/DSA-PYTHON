def max_in_list(l:list)->int:
    max=l[0]
    for i in l:
        if i>max:
            max=i
    return max
l=[98,101,55,22,121,3,2,2,4,5,1414]
print(max_in_list(l))