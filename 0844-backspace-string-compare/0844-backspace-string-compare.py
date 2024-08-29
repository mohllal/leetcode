class Solution:
    # O(n+m) time and O(n+m) space
    # where n and m are the lengths of the two input strings respectively
    def backspaceCompareLinearTimeAndLinearSpace(self, s: str, t: str) -> bool:
        def removeBackspaces(string: str) -> str:
            string_new = ""
            string_backspaces = 0
        
            current = len(string) - 1
            while current >= 0:
                if string[current] == "#":
                    string_backspaces += 1
                elif string_backspaces > 0:
                    string_backspaces -= 1
                else:
                    string_new += string[current]

                current -= 1
            
            return string_new[::-1]
        
        s_new = removeBackspaces(s)
        t_new = removeBackspaces(t)

        return s_new == t_new
    
    # O(n+m) time and O(1) space
    # where n and m are the lengths of the two input strings respectively
    def backspaceCompareLinearTimeAndConstantSpace(self, s: str, t: str) -> bool:
        def getNextValidIndex(string: str, index: int) -> int:
            backspaces = 0
            while index >= 0:
                if string[index] == "#":
                    backspaces += 1
                elif backspaces > 0:
                    backspaces -= 1 # found a character that is affected by a backspace, skip it
                else:
                    break # found a valid character that is not affected by any backspace
                index -= 1

            return index
        
        current_s = len(s) - 1
        current_t = len(t) - 1
        while current_s >= 0 or current_t >= 0:
            current_s = getNextValidIndex(s, current_s)
            current_t = getNextValidIndex(t, current_t)
        
            # if both pointers have valid characters, compare them
            if current_s >= 0 and current_t >= 0 and s[current_s] != t[current_t]:
                return False
            
            # if one string has a valid character left and the other doesn't,
            if (current_s >= 0 and current_t < 0) or (current_t >= 0 and current_s < 0):
                return False
            
            current_s -= 1
            current_t -= 1
        
        return True
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.backspaceCompareLinearTimeAndConstantSpace(s, t)