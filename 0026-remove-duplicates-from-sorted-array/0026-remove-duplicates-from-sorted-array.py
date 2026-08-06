class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        
        k=0

        for p in range(1,len(nums)):
            if nums[p]!=nums[k]:
                k+=1
                nums[k]=nums[p]
        return k+1

        
    
            

                

    
        