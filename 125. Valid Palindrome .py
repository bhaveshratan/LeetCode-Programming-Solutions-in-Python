'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

'''

# Method 1

class Solution:

    def isPalindrome(self, s: str) -> bool:

        if s == '' : return True

        phrase = ''

        for i in s : 

            try : 

                p = int(i)

                phrase = phrase + i

            except : 

                if (i>='A' and i<='Z') or (i>='a' and i<='z') :

                    phrase = phrase + i

        phrase = phrase.lower()

        if phrase == phrase[::-1] : return True

        else : return False

# Method 2

class Solution:

    def isPalindrome(self, s: str) -> bool:

        phrase = ''

        for i in s : 

            if i.isalnum() == True : phrase += i.lower()


        return phrase == phrase[::-1]
