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
            
                    
    
    @property
    def peek(self):
        if self.isempty:
            print("Operation failed")
            return
        print("Head:",self.head.data)
        
        
a=LinkedList()
a.display
a.delete_head()
a.append_back(20)
a.delete_head()
a.append(30)
a.append(40)
a.append(50)
a.display
a.peek
a.append(60)
a.append_back(20)
a.append_back(10)
a.delete_head()

a.display
a.delete_back()
                