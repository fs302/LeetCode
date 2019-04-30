class Solution(object):
    def seperatePattern(self, p):
        ''' Preprocessing for cutting patterns into segmants'''
        patterns = []
        i = 0
        cur_pattern = ''
        while i < len(p):
            if p[i]=='*' or len(cur_pattern) == 0:
                cur_pattern = cur_pattern + p[i]
            else:
                patterns.append(cur_pattern)
                cur_pattern = p[i]
            i += 1
        patterns.append(cur_pattern)
        return patterns
    
    def patternCheck(self, s, patterns, depth = 0):
        ''' Implement a full check on s according to processed patterns'''
        pt = patterns[0]
        # print depth, s,'\t',patterns
        if len(s)>0 and (s[0] == pt[0] or pt[0] == '.') and len(pt) == 1:
            if len(s) == 1 and len(patterns) == 1: 
                return True  # leave-1
            elif len(s) > 1 and len(patterns) == 1:
                return False # leave-2
            else:
                return self.patternCheck(s[1:], patterns[1:], depth+1)
        elif len(pt) > 1:
            if len(patterns) == 1: # final match
                i = 0
                while i < len(s) and (s[i] == pt[0] or pt[0] == '.'):
                    i += 1
                if i==len(s):
                    return True #leave-3
            else:
                i = 0
                flag = False
                while i < len(s):
                    flag = self.patternCheck(s[i:], patterns[1:], depth+1) 
                    if flag == True:
                        return True 
                    if s[i] == pt[0] or pt[0]=='.':
                        i += 1
                    else:
                        break
                flag = self.patternCheck(s, patterns[1:], depth+1) 
                return flag 
        else:
            return False
        return False
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==0 and len(s)>0:
            return False
        
        if len(p)==0 and len(s)==0:
            return True
        
        patterns = self.seperatePattern(p)
        # print patterns
        
        check_label = self.patternCheck(s, patterns)
        return check_label
        

def stringToString(input):
    return input[1:-1].decode('string_escape')

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            line = lines.next()
            p = stringToString(line)
            
            ret = Solution().isMatch(s, p)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()