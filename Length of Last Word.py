'''
58. Length of Last Word

https://leetcode.com/problems/length-of-last-word/

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s1 = s.strip()
        s2 = s1.split(" ")
        s3 = s2[len(s2)-1]
        s4 = len(s3)

        return s4
