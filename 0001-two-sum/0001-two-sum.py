class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        freq={}

        for i in range(len(nums)):
            num=nums[i]
            complement=target-num

            if complement in freq:
                return [freq[complement],i]
                
            freq[num] = i
            
            

    
        