class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """
        n=len(nums)
        k=k%n

        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(0,n-1)  #remember reverse entire array
        reverse(0,k-1)  #reverse the first k 
        reverse(k,n-1) #reverse the remaining