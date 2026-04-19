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


            

    
    
