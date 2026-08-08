class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0 
        x = 0
        sign = 1

        while i < len(s) and s[i] == " ":
            i += 1
        
        if i < len(s) and s[i] == "-":
            sign = -1
            i +=1
        elif i < len(s) and s[i] == "+":
            i += 1
        while i < len(s) and s[i].isdigit():
             x = x * 10 + int(s[i])
             i += 1
        
        x = x* sign
        if x < -2147483648:
            return -2147483648
        if x > 2147483647:
            return 2147483647
        return x