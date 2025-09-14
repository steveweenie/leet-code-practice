class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(s1, s2) -> int:
            while s2:
                s1, s2 = s2, s1 % s2
            return s1
        
        return str1[:gcd(len(str1),len(str2))]
    

