class root:
    pass

class studentTree:       
    pass
        


class student(studentTree):
    def __init__(self,capacity=10):
        self.capacity=capacity#storing capacity of the class lets assume maximum 50 students are there
        self.size=0#to record actual size of class
        self.bucket=[[] for i in range(capacity)]#a list having 50nested list 
        #print(self.bucket)

    def _hash(self,roll_no):
        return hash(roll_no)%self.capacity
    
    def _resize(self):
        old_bucket=self.bucket
        self.capacity*=2
        self.bucket=[[] for i in range(self.capacity)]
        print(self.bucket)
        self.size=0
        for i in old_bucket:
            for key,value in i:
                self.insert_name(key,value)
    
    def insert_name(self,roll_no,name):
        if self.size/self.capacity>0.75:
            self._resize()
            print("resize succesfully")
        
        index=self._hash(roll_no)
        bucket=self.bucket[index]
        for i,(r_no,nam) in enumerate(bucket):
            if r_no==roll_no:
                bucket[i]=(r_no,nam.title())
                return
        bucket.append((roll_no,name.title()))
        self.size+=1
    
    def get(self,roll_no):
        index=self._hash(roll_no)
        bucket=self.bucket[index]
        for r_no,nam in bucket:
            if r_no==roll_no:
                print(nam)
                return
        print("student doesno exist")
    
    def remove(self,roll_no):
        index=self._hash(roll_no)
        bucket=self.bucket[index]
        for i,(r_no,_) in enumerate(bucket):
            if r_no==roll_no:
                print(f"student {_} roll no {r_no} is removed")
                del bucket[i]
                self.size-=1
                return
        print("student does not exist")    
    
    def class_list(self):
        for i in range(1,self.size+1):
            bucket=self.bucket[self._hash(i)]
            for r_no,nam in bucket:
                print(f"Roll No.:{r_no} \t Name:{nam}")
                
            
    
    
class2=student()
class2.insert_name(1,"abhisekh dubey")                
class2.insert_name(2,"abhisekh chauhan")
print(class2.bucket)                
class2.get(2)
class2.get(1)
class2.class_list()
