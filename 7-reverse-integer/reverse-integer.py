class Solution:
    def reverse(self, x: int) -> int:
        d = 0
        new = 0
        if x > 0 :
            n = x
            while n :
                d = n % 10
                n = n // 10
                new = new *10 + d
            if new > 2147483647:
                return 0
            return new
        if x < 0 :
            n = abs(x)
            while n :
                d = n % 10
                n = n // 10
                new = new *10 + d
            if new > 2147483647:
                return 0
            return -new
        
        return 0

        