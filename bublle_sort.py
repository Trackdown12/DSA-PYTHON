def Bubble_sort(list1:list)->list|str:
    swapped=False
    for i in range(0,len(list1)):
        
        for j in range(0,len(list1)-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
                swapped=True
        if not swapped:
            print(swapped)
            print("already sorted")
            break
    return list1
l=[33,21,32,45,4]
l2=[2,3,4,5,6,74]
print(not True)
print(Bubble_sort(l))
print(Bubble_sort(l2))