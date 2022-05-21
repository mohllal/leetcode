class Solution:
    # O(n) time and O(n) space
    def isValid(self, s: str) -> bool:
        openings = '({[';
        pairs = { '(': ')', '{': '}', '[': ']' };
        stack = [];
        for char in s:
            if char in openings:
                stack.append(char);
            else:
                if not stack:
                    return False;

                last = stack.pop();
                if pairs[last] != char:
                    return False;
        if stack:
            return False;
        else:
            return True