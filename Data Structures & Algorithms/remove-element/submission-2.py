class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k]= nums[i]
                k+=1
        return k


'''
given int array:nums
int: val

=> remove all val from nums IN PLACE
AFTER REMOVE ALL VAL, return the number of remaining elem (k)

IDEAS:
We dont wanna use remove function because it will cause O(n), together with for loop, its gonna be O(n^2) => not optimized

thinking of using 2 ptr
l=0, r 0-> len(nums)-1

if the left ptr reach the num that = val, it will stop there and wait until the right ptr reach the num that !=val and swap it
after that, we can move the left tpr by 1

return l (which is = length of nums after remove)


'''

def remove_elem(nums,val):
    l=0

    for r in range(len(nums)):
        if nums[r]==val:
            continue
        else:
            nums[l]=nums[r]
            l+=1
    return l
        

    































































