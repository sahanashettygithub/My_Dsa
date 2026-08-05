class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consecutive = 0
        maximum = 0

        for num in nums:
            if num == 1:
                consecutive += 1
                if consecutive > maximum:
                    maximum = consecutive
            else:
                consecutive = 0

        return maximum