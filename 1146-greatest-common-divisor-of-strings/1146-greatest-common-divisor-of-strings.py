class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        for i in range(min(len(str1), len(str2)), 0, -1):
            candidate = str1[:i]
            if str1 == candidate * (len(str1) // i) and str2 == candidate * (len(str2) // i):
                return candidate
        return ""