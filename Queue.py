from typing import Optional
class Node:
    def __init__(self,data)->None:
        self.prev=None
        self.data=data
        self.next=None
class Queue:
    def __init__(self)->None:
        self.head=None
        self.tail=None
        self.count=0    
    @property    
    def isEmpty(self)->bool:
        return self.head==None
        
    def append(self,data:int)->None:
        NewNode=Node(data)
        if self.isEmpty:
            self.head=self.tail=NewNode
        else:
            self.tail.next=NewNode
            NewNode.prev=self.tail
            self.tail=NewNode
        self.count+=1
            
    def __str__(self)->str:
        if self.isEmpty:
            return "None"
        temp=self.head
        result=""
        while temp:
            result+=str(temp.data)+"->"
            temp=temp.next
        return result+"None"
    
    @property
    def peekhead(self)->Optional[int]:
        return None if self.isEmpty else  self.head.data
            
        
    
    @property
    def peektail(self)->Optional[int]:
        if self.isEmpty:
            return None
        return self.tail.data
    
    def deque(self)->Optional[int]:
        if self.isEmpty:return None
        
        temp=self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None  # Queue became empty
        self.count-=1
        return temp
    
    def __len__(self):
        return self.count
    
    def clear(self):
        self.head=self.tail=None
        self.count=0
    
    #method that can iterate through queue    
    def __iter__(self):
        temp=self.head
        while temp:
            yield temp.data
            temp=temp.next
    
    def __reversed__(self):
        temp=self.tail
        while temp:
            yield temp.data
            temp=temp.prev
    
a=Queue()
a.append(12)       
a.append(13)       
a.append(14)       
a.append(15)       
a.append(16)
for i in a:
    print(i)       
    
for i in reversed(a):
    print(i)
print(sum(a))