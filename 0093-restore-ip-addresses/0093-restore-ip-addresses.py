class Solution:
    def insert_dot(self, string, index):
        return string[:index] + '.' + string[index:]

    def isValidIP(self, s):
        ip = s.replace('.', ' ').split()
        
        if len(ip) != 4:
            return False
        
        for div in ip:
            if len(div) > 1 and div[0] == '0':
                return False
            
            if int(div) > 255:
                return False

        return True
            
    def backtrack(self, s, subsets):
        if s.count('.') == 5:
            return
     
        if self.isValidIP(s):
            subsets.add(s)
            return    
        else:
            last = s.rfind('.')
            
            oneDigitDiv = self.insert_dot(s, last + 2)
            self.backtrack(oneDigitDiv, subsets)
            
            twoDigitDiv = self.insert_dot(s, last + 3)
            self.backtrack(twoDigitDiv, subsets)

            threeDigitDiv = self.insert_dot(s, last + 4)
            self.backtrack(threeDigitDiv, subsets)

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        
        subsets = set()
        self.backtrack(s, subsets)
        return [str(i) for i in subsets]
