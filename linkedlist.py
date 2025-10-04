class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    @property
    def isempty(self):
        return self.head==None
    
    
    def append(self,data):
        New_Node=Node(data)
        New_Node.next=self.head
        self.head=New_Node
    
    
    def append_back(self,data):
        New_Node=Node(data)
        if self.isempty:
            self.head=New_Node
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=New_Node
    
    @property
    def display(self):
        if self.isempty:
            print("Empty")
            return
        temp=self.head
        while temp:
            print(temp.data,"->",end=" ")
            temp=temp.next
        print("None")
     

    def delete_head(self):
        if self.isempty:
            print("Failed Attempt. List is empty")
            return
        print("deleting head=",self.head.data)
        self.head=self.head.next
        
    def delete_back(self):
        if self.isempty:
            print("Failed Attempt. List is empty")
            return
        elif self.head.next==None:
            print("Deleting Only Node =",self.head.data)
            self.head=None
            return
        else:
            temp=self.head
            while temp.next.next !=None:
                temp=temp.next
                
            print("Deleting Last Node:",temp.next.data)
            temp.next=None
            
    def delete_specific(self,key):
        if self.isempty:
            print("Failed Attempt. List is Empty")
            return
        if self.head.data==key:
            print(f"Deleting {key} Node ")
            self.head=self.head.next
        else:
            temp=self.head
            temp_nxt=self.head.next
            while temp_nxt!=None:
                if temp_nxt.data==key:
                    print(f"Deleting {key} Node ")
                    temp.next=temp_nxt.next
                    break
                temp=temp_nxt
                temp_nxt=temp_nxt.next
                
    
    @property
    def peek(self):
        if self.isempty:
            print("Operation failed")
            return
        return f"Head:{self.head.data}"
    
 
    def __len__(self):
        count=0
        temp =self.head
        while temp:
            count+=1
            temp=temp.next
        return count
    
    def __str__(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return " -> ".join(result) + " -> None"

a=LinkedList()
a.append(12)
a.append(12)
a.append(12)
print(len(a))
a.display
print(a)