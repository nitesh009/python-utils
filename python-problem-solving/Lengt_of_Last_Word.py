class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.rsplit(None, 1)
        return len(words[-1]) if words else 0
        
