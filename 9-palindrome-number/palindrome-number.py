class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_rev = str(x)[::-1]
        if x_rev == str(x):
            return True
        else:
            return False