class Solution:
    def __init__(self):
        self.memory = {}
    
#   def numDecodings(self, s: str) -> int:
#        '''
#        Memorized Search Version
#        '''
#       if s in self.memory:
#           return self.memory[s]
#       # 构建映射表
#       digit_map = {str(i):chr(ord('A')+i-1) for i in range(1,27)}
#       number_of_ways = 0
#       if len(s) >= 1 and len(s) <= 2:
#           if len(s) == 2:
#               if s[0] in digit_map and s[1] in digit_map:
#                   number_of_ways += 1
#           number_of_ways += 1 if s in digit_map else 0
#           self.memory[s] = number_of_ways
#           return number_of_ways
#       candidates = [s[0]]
#       if len(s) > 1:
#           candidates.append(s[:2]) 
#       for c_rep in candidates:
#           if c_rep in digit_map:
#               number_of_ways += self.numDecodings(s[len(c_rep):])
#       self.memory[s] = number_of_ways
#       return number_of_ways


    def numDecodings(self, s: str) -> int:
        '''
        Dynamic Programming Version
        '''
        digit_map = {str(i):chr(ord('A')+i-1) for i in range(1,27)}
        f = [0 for i in range(len(s)+1)]
        len_of_str = len(s)
        # initialization
        if len(s) >= 1:
            f[1] = 1 if s[len_of_str-1] in digit_map else 0
        if len(s) >= 2:
            v = 0
            if s[len_of_str-1] in digit_map and s[len_of_str-2] in digit_map:
                v += 1
            if s[len_of_str-2:] in digit_map:
                v += 1
            f[2] = v
        # back-tracing
        for i in range(3, len(s)+1):
            v = 0
            if s[len_of_str-i] in digit_map:
                v += f[i-1]
            if i >= 1 and s[len_of_str-i:len_of_str-i+2] in digit_map:
                v += f[i-2]
            f[i] = v
        return f[len(s)]

if __name__ == '__main__':
    s = Solution()
    input_str = '1111111111111111111111111111111111111111111'
    res = s.numDecodings(input_str)
    print(input_str, res)