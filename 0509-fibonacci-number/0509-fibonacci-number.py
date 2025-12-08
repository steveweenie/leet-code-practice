class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        table = [0, 1]
        for i in range(2, n + 1):
            F_n = table[i - 1] + table[i - 2]
            table.append(F_n)
        
        return table[n]