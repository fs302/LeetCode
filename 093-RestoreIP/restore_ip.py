from typing import List

class Solution:
    def search_sub_array(self, s, num):
        def valid_num(s):
            return True if len(s)>0 and str(int(s)) == s and int(s) <= 255 else False
        candidates = []
        if num == 1:
            if valid_num(s):
                candidates.append(s)
            return candidates
        for i in range(min(3,len(s))):
            if valid_num(s[:i+1]):
                head = s[:i+1]
                sub_array = self.search_sub_array(s[i+1:], num-1)
                for item in sub_array:
                    candidates.append(head+'.'+item)
        return candidates
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.search_sub_array(s, 4)

if __name__ == '__main__':
    s = Solution()
    input_str = '1111'
    res = s.restoreIpAddresses(input_str)
    print(input_str, res)