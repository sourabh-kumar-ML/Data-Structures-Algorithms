class HashMap:
    def __init__(self,size = 100):
        self.size = size
        self.arr = [None for i in range(self.size)]

    def get_hash(self,key):
        sum_ = 0
        for char in key:
            sum_ += ord(char)
        return sum_ % self.size


    def __setitem__(self,key,item):
        idx = self.get_hash(key)
        self.arr[idx] = item

    def __getitem__(self,key):
        idx = self.get_hash(key)
        return self.arr[idx]

    def __delitem__(self,key):
        idx = self.get_hash(key)
        self.arr[idx] = None


hmap = HashMap()

hmap['sourabh'] = 1
hmap['kumar'] = 2

del hmap['kumar']
