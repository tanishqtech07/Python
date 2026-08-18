#question no. 2357

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        new = set() #Create empty set, jiske andar unique elements
        for i in nums:
            if i == 0: #agar list mai 0 aata hai toh usse list mai add nahi karenge
                continue
            else:
                new.add(i)
        
        return len(new) #jitne set mai elemets hai utne operations lag rhe hai.
    
    
#question no. 2206

# 1st we create a empty dictionary d={}
#we check frequency of each element in the list and store it in the dictionary
#dictonary mai key as element and value as frequency(values par lopp lagay ge) d.values()

 