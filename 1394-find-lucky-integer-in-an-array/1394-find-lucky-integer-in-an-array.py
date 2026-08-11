class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        lucky = -1

        for num in freq:
            if freq[num] == num:
                lucky=num

        return lucky