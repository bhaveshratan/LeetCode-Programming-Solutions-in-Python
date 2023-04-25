'''

58. Length of Last Word

https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s1 = s.strip()
        s2 = s1.split(" ")
        s3 = s2[len(s2)-1]
        s4 = len(s3)

        return s4
