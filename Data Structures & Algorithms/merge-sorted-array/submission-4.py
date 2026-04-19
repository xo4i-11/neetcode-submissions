class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        last=m+n-1

        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
                
            last-=1

        #fill num1 with leftover nums2 elements
        while n>0:
            nums1[last]=nums2[n-1]
            n-=1
            last-=1
        
        
"""
special case: nums1=[10,12,14,0,0], nums2=[1,2]
=> m decrese but n not decrease => add them in the front afterwards
"""

"""


        last=m+n-1

        while m>0 and n>0:
            if nums2[n-1] > nums1[m-1]:
                nums1[last]=nums2[n-1]
                n-=1
            
            else:
                nums1[last]=nums1[m-1]
                m-=1
            
            last-=1

        while n>0:
            nums1[last]=nums2[n-1]
            n-=1
            last-=1
"""




            






















































        