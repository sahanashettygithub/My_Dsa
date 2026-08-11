class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={}

        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1

        for char in s:
            if freq[char]==1:
                return s.index(char)
        return -1
        