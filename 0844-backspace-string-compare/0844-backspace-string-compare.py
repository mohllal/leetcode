class Solution:
    # O(n) time and O(n) space
    def backspaceCompareLinearTimeAndLinearSpace(self, s: str, t: str) -> bool:
        def removeBackspaces(string: str) -> str:
            string_new = ""
            string_backspaces = 0
        
            current = len(string) - 1
            while current >= 0:
                if string[current] == "#":
                    string_backspaces += 1
                else:
                    if string_backspaces > 0:
                        string_backspaces -= 1
                    else:
                        string_new += string[current]

                current -= 1
            
            return string_new[::-1]
        
        s_new = removeBackspaces(s)
        t_new = removeBackspaces(t)

        return s_new == t_new
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.backspaceCompareLinearTimeAndLinearSpace(s, t)