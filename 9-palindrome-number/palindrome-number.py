class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        a = 0
        while n != 0 :
            d = n % 10
            a = a * 10 + d
            n = n // 10
        
        if a == x:
            return True
        
        return False





        