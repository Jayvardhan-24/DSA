class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        sign = -1 if x < 0 else 1
        rev = str(abs(x))[::-1]
        rev_int = sign * int(rev)

        if rev_int < MIN or rev_int > MAX:
            return 0
    
        return rev_int