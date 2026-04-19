#chaining 
class Hashmap:
    def __init__(self,capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)] 
        #this line will create
        """[
        [], [], [], [], [], [], [], [], [], []
           ]"""
        
    def _hash(self,key):
        return hash(key)%self.capacity
    
    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self,key,value):
        index=self._hash(key)
        print("index=",index)
        buckets=self.buckets[index]
        print("bucket=",buckets)
        for i, (k, v) in enumerate(buckets):
            if k == key:
                buckets[i] = (key, value)
                return

        buckets.append((key, value))
        self.size += 1
        
    def get(self, key):
        index = self._hash(key)
        buckets = self.buckets[index]
        for k, v in buckets:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False
a=(enumerate("str"))
for i in a:
    print(type(i))
hm = Hashmap()
hm.insert("name", "Vinay")
print(hm.get("name"))  # Vinay
hm.insert("name", "kumar")
hm.insert("age", 21)
hm._resize()
print(hm.get("name"))  # Vinay
print(hm.get("age"))  # 21
hm.remove("age")
