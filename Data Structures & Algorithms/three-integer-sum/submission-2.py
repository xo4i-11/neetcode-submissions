class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res=[]
        nums.sort()

        for i in range(len(nums)):
            if(nums[i]>0): #since if nums[i]>0, all the next num will be >0 => cannot create a sum of 0
                break

            if(i>0 and nums[i]==nums[i-1]): #check if there is duplicate or no
                continue
            
            l=i+1
            r=len(nums)-1
            while(l<r):
                total= nums[i]+ nums[l]+ nums[r]
                if(total<0):
                    l+=1
                elif(total>0):
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    #[-1,-1,0,0,1,1]
                    l+=1
                    while nums[l]== nums[l-1] and l<r:
                        l+=1
            
        return res








"""

res=[]
num.sort()
#[-4,-1,-1,0,1,2]

for i in range (len(nums)):
    #when we see a value that is greater than 0 => sum of them will not be 0
    if nums[i]>0:
        break

    if i>0 and nums[i]==nums[i-1]: #we check if there is any dupllicate or no. if not, we can skip the loop
        continue
    
    l=i+1
    r=len(nums)-1
    while l<r:
        total=nums[l]+nums[r]+nums[i]
        if total>0:
            r-=1
        if total<0:
            l+=1
        else:
            res.append([nums[i],nums[l],nums[r]])
            #[-1,-1,0,0,1,1]
            l+=1
            while nums[l]==nums[l-1] and l<r:
                l+=1
            



return res





#IDEAS:

Since we wanna use 2 pointer => we need to sort the array
- sort the array O(n.log(n))
- for each number inside the array, we gonna find 2 other ptr that make them to have the sum of 0
=> loop through every elem in array, left_ptr=i+1, right_ptr=len(arr)-1

- if the current elem is >0 => break since every other elem will also >0 and does not the sum to be 0

- if the left neighbor = the current elem => they are not allow to be duplicate => we gonna skip the loop using "continue"
example: [-1,0,1,2,-1,-4] =>  after sort: [-4,-1,-1,0,1,2]
when i=1 => nums[i]=-1 => the valid sum is: [-1,0,1]
when i=2 => nums[i]=-1 => valid sum is: [-1,0,1] => duplicate => we need to skip this

- while l<r:

    + if sum too large => move right ptr
    + if sum too small => move left ptr

    + else if sum==0 => append that pair to the returned list
        after that, we would need to move both ptr in order to find a new valid pair
        if the left neighbor = current left ptr => l+=1
        ex: [-1,0,0,0,1] 
        #when l 


# Constaint:
# i,j,k are different (elem can be the same)
# does not include duplicate triplet 
# it can be in any order

def three_sum(nums):
    nums.sort() # O(N.log(N))
    res=[]


    #make sure the sum=0
    for i in range(len(nums)):
        if nums[i]>0:
            break
        
        if i>0 and nums[i]==nums[i-1]:
            continue
        
        l=i+1
        r=len(nums)-1

        while l<r:
            total = nums[i]+ nums[l] + nums[r]

            if l<r and total>0:
                r-=1
            
            elif l<r and total<0:
                l+=1
            
            else:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1


                while l<r and nums[l]==nums[l-1]:
                    l+=1
    return res



"""

        




















































