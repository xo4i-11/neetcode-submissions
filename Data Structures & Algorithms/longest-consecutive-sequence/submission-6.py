class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ##IDEAS:
        # check the left neighbor of every value in the list to figure out if it is a start of a sequence or not
        #for ex:
        # [100,4,200,1,3,2]
        # 100->
        # 200->
        # 1->2->3->4->

        numSet=set(nums) #since searching in a set cost O(1)
        longest=0
        for n in numSet:
            #check if it is the start of a sequence or no
            if(n-1 not in numSet):
                length=0
                while (n+length) in numSet: #check if the next num is in the list or no (O(1))
                    length+=1
                longest=max(length,longest)
        return longest




#IDEAS:
# nums=[2,20,4,10,3,4,5] 
#we want it all the elem to be unique => change it to the set 
# finding the first number of the streak =>means that it have no left neighbor 
#for example: 2 3 4 4 5 => streak =4 ( we want to remove the number 4 since it is not necessary -> change nums to set)
#we gonna do the same with every elements in num 
#to find the streak, we need to check if the elem has right neighbor or not. if it has, +1 to the sreak

"""
Ideas:
change the nums to set to make sure the elems are unique
loop through every num in nums
find the first elem of the longest sequence => find the elem that does not have left neighbor in the set
create variable length=0 to track the length of that sequence
keep checking if (first elem in the sequence + length) is in the set or not;
if yes: length+=1
finally, compare the the variable "longest" to track the longest sequence exist 


 def longest_sequence(nums):
    longest=0
    numSet=set(nums)
    
    for num in nums:
        if n-1 not in numSet:
            length=0
            while n+length in numSet:
                length+=1
            longest=max(length,longest)
    return longest

"""   



































