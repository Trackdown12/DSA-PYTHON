class Node:
    def __init__(self,value):
        self.left=None
        self.value=value
        self.right=None
        
        
class Tree():
    def __init__(self):
        self.count=0
        self.root=None
    
    
    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
            self.count+=1
            return
        self._insert(self.root,value)
        self.count+=1
             
    def _insert(self,root,value):
        if value<=root.value:
            if root.left:
                self._insert(root.left,value)
            else:
                root.left=Node(value)
        elif value>root.value:
            if root.right :
                self._insert(root.right,value)
            else:
                root.right=Node(value)                
    
    def inorder(self):
        for i in self._inorder_gen(self.root) :
            print(i)
        
    
         
    def preorder(self):
        for i in self._preorder_gen(self.root):
            print(i)
     
    def _preorder_gen(self, root):
        if root is None:
            return
        yield (root.value)
        yield from self._preorder_gen(root.left)
        yield from self._preorder_gen(root.right)

    def postorder(self):
        for i in self._postorder_gen(self.root):
            print(i)
        
    def _postorder_gen(self,root):
        if root is None:
            return
        yield from self._postorder_gen(root.left)
        yield from self._postorder_gen(root.right)
        yield (root.value)
    
    @property
    def min(self):
        if self.root is None:
            raise ValueError("empty")
        root=self.root
        while root.left is not None:
            root=root.left
        return root.value
    
    @property
    def max(self):
        if self.root is None:
            raise ValueError("empty")
        root=self.root
        while root.right is not None:
            root=root.right
        return root.value
    
    def __contains__ (self,value):
        root = self.root
        while root is not None:
            if value==root.value:
                return True
            root = root.left if value < root.value else root.right
        return False

    
    
    def _delete(self,root,value):
        parent=None
        while root is not None:
            if root.value==value:
                break
            parent=root
            root = root.left if value < root.value else root.right
        else:
            raise ValueError("value dooet exists")
        
        if (root.left is None) and (root.right is None):
            return self._leafdel(parent,root)
        elif (root.left is not None) and (root.right is None):
            return self._oneLeftdel(parent,root)
        elif (root.left is  None) and (root.right is not None):
            return self._oneRightdel(parent,root)
        elif (root.left is not None) and (root.right is not None):
            return self._twodel(root)
        
        
    def _leafdel(self,parent,root):
        if parent is None:
                self.root=None
                return True
            
        elif parent.right==root:
            parent.right=None
            
        elif parent.left==root:
            parent.left=None
        return True
    
    def _oneLeftdel(self,parent,root):
        if parent is None:
            self.root=root.left
            return True
        elif parent.left==root :
            parent.left=root.left
        elif parent.right==root :
            parent.right=root.left
        return True
    
    def _oneRightdel(self,parent,root):
        if parent is None:
            self.root=root.right
            return True
        elif parent.left==root :
            parent.left=root.right
        elif parent.right==root :
            parent.right=root.right        
        return True
    
    def  _inordersuccessor(self,root):
        temp=None
        while root.left is not None:
            temp=root
            root=root.left
        return temp,root
    
    def _twodel(self,root):
        
        inorder_successor_parent,inorder_successor=self._inordersuccessor(root.right)
        root.value=inorder_successor.value
        if inorder_successor_parent is None:
            # successor is direct right child
            root.right = inorder_successor.right
            return True

        if inorder_successor.right is not None:
            return self._oneRightdel(inorder_successor_parent,inorder_successor)
        else:
            return self._leafdel(inorder_successor_parent,inorder_successor) 
    
            
    
    def delete(self,value):
        if self.root==None:
            raise ValueError("Empty")
        deletion=self._delete(self.root,value)
        if deletion:
            self.count-=1
            return deletion
        else:
            raise ValueError("Deletion Failed")
        
    def _inorder_gen(self,root):
        if root is None:
            return 
        yield from self._inorder_gen(root.left)
        yield(root.value)
        yield from self._inorder_gen(root.right)
        
    def __iter__(self):
        return self._inorder_gen(self.root)
    
    def bst_to_list(self):
        if self.root is None:
            raise ValueError("tree is empty")
        else:
            return list(self)
        
    def __len__(self):
        return self.count
    
    def height(self):
        if self.root is None:
            return -1
        return self._height(self.root)
    def _height(self,root):
        if root is None:
            return-1
        return 1+max(self._height(root.left),self._height(root.right))
            
t=Tree()
t.inorder()
t.insert(12)     
t.insert(5)     
t.insert(4)     
t.insert(6)     
t.insert(17) 
t.insert(15) 
t.insert(16) 
print(12 in t)
print(11 in t)
print(17 in t)
print("hieght=",t.height())
print("inorder")
t.inorder()
print("preorder")
t.preorder()
print("postorder")
t.postorder()
print(t.min)    
print(t.max)
print(t.delete(15))
print("inorder")
t.inorder()
print("tree in loop")
for i in t:
    print(i)
a=t.bst_to_list()
print(a)
