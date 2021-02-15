class Seperate_HashMap:
    def __init__(self,size = 10):
        print("Sepearate Chaining Method")
        self.size = size
        self.arr = [[] for i in range(self.size)]

    def get_hash(self,key):
        sum_ = 0
        for char in key:
            sum_ += ord(char)
        return sum_ % self.size


    def __setitem__(self,key,item):
        idx = self.get_hash(key)
        if len(self.arr[idx]) != 0:
            
            for index,value in enumerate(self.arr[idx]):
                if value[0] == key:
                    self.arr[idx][index] = (key,item)
                else : self.arr[idx].append((key,item))
                    
        else:
            self.arr[idx].append((key,item))

    def __getitem__(self,key):
        idx = self.get_hash(key)
        for index,value in enumerate(self.arr[idx]):
            if value[0] == key:
                return self.arr[idx][index]

    def __delitem__(self,key):
        idx = self.get_hash(key)
        self.arr[idx] = []


hmap = Seperate_HashMap()

hmap['key 1'] = 1
hmap['key 3'] = 110
hmap['key 2'] = 5


