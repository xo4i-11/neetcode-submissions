class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return
        

    






"""
ideas:
    - for example, we are given an array:
        [1, 3, 4, 2, 2]
    
    - We now assign the idx to them:
        [  1,  3,   4,   2,   2]
           0   1    2    3    4
    
    - since every intger appear once, then in the array n+1 will have 1 dup num
    => from array, we construct linkedlist such that:
        + the val of node = the elem in array
        + the pointer point to value at the idx= node's value
            for ex: [  1,  3,   4,   2,   2]
                       0   1    2    3    4       

            => Linkedlist: 1 -> 3 -> 2 -> 4  
                                     ^    |
                                     |    |     
                                      -----  
        

    



"""
        
    

        