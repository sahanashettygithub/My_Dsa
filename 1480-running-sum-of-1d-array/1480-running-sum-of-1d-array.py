class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=[]
        sum=0

        for i in range(len(nums)):
            sum+=nums[i]
            answer.append(sum)
        return answer