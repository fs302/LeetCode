import re
class Solution:
    def isInt(self, s):
        pattern = re.compile("[-+]?[0-9]+")
        res = re.fullmatch(pattern, s) is not None
        return res
        
    def isDouble(self, s):
        pattern = re.compile("[-+]?[0-9]+\.?[0-9]*|[-+]?[0-9]*\.?[0-9]+")
        res = re.fullmatch(pattern, s) is not None
        return res
    
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        parts = s.split('e')
        if len(parts) > 1:
            if len(parts) > 2:
                return False
            ex_part = parts[1]
            if not self.isInt(ex_part):
                return False
        base_part = parts[0]
        if not self.isDouble(base_part):
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isNumber("0.145"))