""" 
WAP A PROGRAM TO FIND THE POSITION OF A GIVEN NUMBER IN THE LIST OF NUMBERS ARRANGED IN DESCENDING ORDER,
ALSO MINIMIZE THE NUMBER OF TIMES WE ACCESS ELEMENTS
"""

def find_position(list1,num):
    list1.sort(reverse=True)#in case of unsorted list passed
    if list1==[]:
        return "list is empty"
    
    beg=0
    mid=None
    end=len(list1)-1 
    while(beg<=end):
        mid=(beg+end)//2
        if list1[mid]==num:
            return list1.index(list1[mid])
        elif num>list1[mid]:
            end=mid-1
        else:
            beg=mid+1
    else:
        return "number does not exist"
    