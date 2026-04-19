def selection_sort(list1:list)->list|str:
    for i in range(0,len(list1)):
        min_term=list1[i]
        swapped=False
        for j in range(i+1,len(list1)):
            if list1[j]<min_term:
                min_term,list1[j]=list1[j],min_term
                swapped=True
        if not swapped:
            print("sorted array")
            break
    return list1
l=[33,21,32,45,4]
l2=[2,3,4,5,6,74]
print(selection_sort(l))
print(selection_sort(l2))