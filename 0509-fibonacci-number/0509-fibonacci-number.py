class Solution:
    def fib(self, n: int) -> int:
        return self.fibLinearTimeAndConstantSpace(n)
    
    # O(2^n) time and O(n) space
    def fibExponentialTimeAndLinearSpace(self, n: int) -> int:
        def fibHelper(n: int) -> int:
            if n <= 1:
                return n

            return fibHelper(n - 1) + fibHelper(n - 2)
        
        return fibHelper(n)
    
    # O(n) time and O(n) space
    def fibLinearTimeAndLinearSpace(self, n: int) -> int:
        def fibHelper(n: int, memo={}) -> int:
            if n <= 1:
                return n
            
            if n in memo:
                return memo[n]
            
            memo[n] = fibHelper(n - 1) + fibHelper(n - 2)
            return memo[n]
        
        return fibHelper(n)
    
    # O(n) time and O(1) space
    def fibLinearTimeAndConstantSpace(self, n: int) -> int:
        fib = [0, 1]
        
        for i in range(2, n + 1):
            current = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = current
        
        return fib[n] if n <= 1 else fib[1]
