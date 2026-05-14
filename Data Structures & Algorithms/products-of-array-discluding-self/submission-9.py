class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array=[]
        zero_counter=0
        product=1
        
        for i in range(len(nums)):
            if (nums[i]==0):
                zero_counter+=1
            else:
                product=nums[i]*product
        
        if(zero_counter>=2):
            return [0]*len(nums)
    
        
        for k in range(len(nums)):
            if(zero_counter==0):
                added_num=product//nums[k]
                array.append(added_num)
            
            elif(zero_counter==1):
                if(nums[k]==0):
                    array.append(product)
                else:
                    array.append(0)
        
        return array


#if not idx, then store it in the array
            

    
    
# nums[1,2,3] => [6,3,2]
# special case: 
# 1) if there is 1 zero => the number at index of 0 will be product of the other 2, follow with 0. ex: [0,2,4] -> [8,0,0]
# 2) if there are >=2 zeros => all the output index=0. ex: [0,0,2,3,4] => [0,0,0,0]





"""
#given an array nun:

#CASE 1: no 0 in nums
#=> [1,2,4,6]
#=> [48,24,12,8]

#CASE 2: 1 0
# [0, 2, 4, 6]
# => [48,0,0,0]

#CASE 3: 2 0
#[0,0,4,6]
#=> [0,0,0,0]
        zero_counter=0
        
        for num in nums:
            if num==0:
                zero_counter+=1
        
        if zero_counter>=2:
            return [0]*len(nums)
        
        
        #we gonna loop through every single value in the list
        #if zero_counter=1
        # the product at the idx of zero gonna be the product of every other number

        res=[]
        product=1

        for k in range (len(nums)):
            if (zero_counter==1 and nums[k]!=0):
                product=product*nums[k]
            elif zero_counter ==0:
                product =product*nums[k]
            

        for i in range (len(nums)):
            if (zero_counter==1):
                if nums[i]==0:
                    res.append(product)
                else:
                    res.append(0)
            
            elif zero_counter==0:
                res.append(product//nums[i])
        
        return res



            
            
        



#given an array nun:

#CASE 1: no 0 in nums
#=> [1,2,4,6]
#=> [48,24,12,8]

#CASE 2: 1 0
# [0, 2, 4, 6]
# => [48,0,0,0]

#CASE 3: 2 0
#[0,0,4,6]
#=> [0,0,0,0]



def prod(nums):
    zero_counter=0
    product=1

    for num in nums:
        if num==0:
            zero_counter+=1
        else:
            product=product*num

    
    if zero_counter>=2:
        return [0]*len(nums)
    

    arr=[]
    for n in nums:
        if zero_counter==0:
            elem=product/n
            arr.append(elem)
        elif zero_counter==1:
            if n==0:
                arr.append(product)
            else:
                arr.append(0)
    return arr

"""
    









"""

product of array except themself:
there will be 3 case:
1 0, >=2 0, 0 0


for the case when >=2 0:
ex: [0,0,1,2,3]
=> 0,0,0,0,0

for the case when 1 0:
ex: [0,1,2,3]
=> [6,0,0,0]

for the case when 0 0:
ex: [1,2,3,4]
=> overall product/ elem
"""

def product_of_array_except_self(nums):
    #trynna find how many number of 0 are there
    zero_count=0
    product =1

    for num in nums:

        if num == 0:
            zero_count+=1
        else:
            product=product*num
    
    if zero_count>=2:
        return [0]*len(nums)
    
    res=[]

    for elem in nums:
        if zero_count==0:
            prod_at_elem= product/elem
            res.append(prod_at_elem)
        elif zero_count==1:
            if elem == 0:
                res.append(product)
            else:
                res.append(0)

    return res








































    
