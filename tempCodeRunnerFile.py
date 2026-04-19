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
            return
        self._insert(self.root,value)
             
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
        self._inorder(self.root) 
        
    def _inorder(self,root):
        if  root is None :
            return
        self._inorder(root.left)
        print(root.value)
        self._inorder(root.right)
         
    def preorder(self):
        self._preorder(self.root)
     
    def _preorder(self, root):
        if root is None:
            return
        print(root.value)
        self._preorder(root.left)
        self._preorder(root.right)

    def postorder(self):
        self._postorder(self.root)
        
    def _postorder(self,root):
        if root is None:
            return
        self._postorder(root.left)
        self._postorder(root.right)
        print(root.value)
    
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
    
    def search(self,value):
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
            return "value does not exists"
        
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
                return f"node is deleted succesfully"
            
        elif parent.right==root:
            parent.right=None
            
        elif parent.left==root:
            parent.left=None
        return f"node is deleted succesfully"
    
    def _oneLeftdel(self,parent,root):
        if parent is None:
            self.root=root.left
            return f"node is deleted succesfully"
        elif parent.left==root :
            parent.left=root.left
        elif parent.right==root :
            parent.right=root.left
        return f"node is deleted succesfully"
    
    def _oneRightdel(self,parent,root):
        if parent is None:
            self.root=root.right
            return f"node is deleted succesfully"
        elif parent.left==root :
            parent.left=root.right
        elif parent.right==root :
            parent.right=root.right        
        return f"node is deleted succesfully"
    
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
            return "node is deleted successfully"

        if inorder_successor.right is not None:
            return self._oneRightdel(inorder_successor_parent,inorder_successor)
        else:
            return self._leafdel(inorder_successor_parent,inorder_successor) 
    
            
    
    def delete(self,value):
        if self.root==None:
            return f"tree does not exists"
        return self._delete(self.root,value)
        
    def tree_to_sorted_list(self):
        pass
    
    def inorder_gen(self,root):
        if root is None:
            return 
        yield from self.inorder_gen(root.left)
        yield(root.value)
        yield from self.inorder_gen(root.right)
        
    def __iter__(self):
        return self.inorder_gen(self.root)
    
    def bst_to_list(self):
        if self.root is None:
            raise ValueError("tree is empty")
        else:
            return list(self)
        
            
t=Tree()
for i in t:
    print(i)
t.inorder()
t.insert(12)     
t.insert(5)     
t.insert(4)     
t.insert(6)     
t.insert(17) 
t.insert(15) 
t.insert(16) 
print(t.search(12))
print(t.search(1))
print(t.search(17))
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