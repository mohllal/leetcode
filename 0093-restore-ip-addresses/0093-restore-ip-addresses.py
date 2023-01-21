class Solution:
    def insertDot(self, string, index):
        return string[:index] + '.' + string[index:]

    def isValidIP(self, s):
        divs = s.replace('.', ' ').split()

        if len(divs) != 4:
            return False

        for div in divs:
            if len(div) > 1 and div[0] == '0':
                return False

            if int(div) > 255:
                return False

        return True

    def backtrack(self, s, subsets):
        if s.count('.') == 3:
            if self.isValidIP(s):
                subsets.add(s)
            return
        else:
            last = s.rfind('.')

            oneDigitDiv = self.insertDot(s, last + 2)
            self.backtrack(oneDigitDiv, subsets)

            twoDigitDiv = self.insertDot(s, last + 3)
            self.backtrack(twoDigitDiv, subsets)

            threeDigitDiv = self.insertDot(s, last + 4)
            self.backtrack(threeDigitDiv, subsets)

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []
        
        subsets = set()
        self.backtrack(s, subsets)
        return [str(i) for i in subsets]
