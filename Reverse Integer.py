'''
7. Reverse Integer

https://leetcode.com/problems/reverse-integer/description/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        
        if x >= 0 : return  int(s[::-1]) if int(s[::-1]) <= (2**31 - 1) else 0
        else: 
                s = str(abs(x))
                return int('-'+s[::-1]) if int(s[::-1]) <= (2**31) else 0
