class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
        self.size=0
    
    @property
    def isEmpty(self):
        return self.top==None
    
    def push(self,data):
        newnode=Node(data)
        newnode.next=self.top
        self.top=newnode
        self.size+=1
     
    def pop(self):
        if self.isEmpty:
            return "UnderFlow"
        temp=self.top
        self.top=self.top.next
        self.size-=1
        return temp.data
        
    def peek(self):
        if self.isEmpty: 
            return " UnderFlow"
        return self.top.data
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.isEmpty: 
            return "UnderFlow"
        temp=self.top
        str1=""
        while temp:
            str1+=str(temp.data)+"->"
            temp=temp.next
        return str1+"None"
    
    def search(self,key):
        if self.isEmpty:
            return "UnderFlow"
        else:
            temp=self.top
            while temp:
                if temp.data==key:
                    return True
                temp=temp.next
            return False
   
s=stack()
s.push(12)                  
s.push(13)                  
s.push(14)                  
s.push(15)                  
s.push(16)
print(s.peek())                  
            
    

        
    
    
               
        