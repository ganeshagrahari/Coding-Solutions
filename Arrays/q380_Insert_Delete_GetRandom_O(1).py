import random
class RandomizedSet(object):
    def __init__(self):
        self.numMap = {}
        self.numList = []
    
    def insert(self,val):
        res = val not in self.numMap
        if res:
            self.numMap[val]=len(self.numList)    # adding in the last dict
            self.numList.append(val) # adding in last in list
        return res
    
    def remove(self,val):
        res = val in self.numMap
        if res:
            idx  = self.numMap[val] # index of a valur to delete
            lastval  = self.numList[-1] # getting last element
            self.numMap[idx]= lastval# moving last to deleted spot
            self.numList.pop() #removing last element   
            self.numMap[lastval]= idx#update the index of moved value
            del self.numMap[val]# delete value from map
        return res
    
    def getrandom(self):
        return random.choice(self.numList)    
    
    
    
#procedure of removing:
'''
🔍 Step-by-step:
Let’s say:

numList = [5, 7, 10]

numMap = {5: 0, 7: 1, 10: 2}
Now you want to remove(7)

idx = 1 (index of 7)

lastval = 10

Replace numList[1] with 10: → [5, 10, 10]

pop() removes last element: → [5, 10]

Update numMap[10] = 1

Delete numMap[7]

Efficient! No shifting like regular list removal.'''    
    