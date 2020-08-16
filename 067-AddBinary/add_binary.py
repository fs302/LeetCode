class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # make a's length longer
        if len(a) < len(b):
            a, b = b, a
        
        l_a = len(a)
        l_b = len(b)
        tmp_digit = 0
        res = []
        for i in range(l_a):
            if i < l_b:
                p = int(a[-i-1]) + int(b[-i-1]) + tmp_digit
            else:
                p = int(a[-i-1]) + tmp_digit
            if p >= 2:
                tmp_digit = 1
                res.append(str(p-2))
            else:
                tmp_digit = 0
                res.append(str(p))
        if tmp_digit >= 1:
            res.append('1')
        return ''.join(res[::-1])
            
        # 1 Line Coder
        # return bin(int(a,2) + int(b,2)).replace("0b","") 

def main():
    a = '1001'
    b = '1110'
    ret = Solution().addBinary(a, b)
    print(ret)

if __name__ == '__main__':
    main()                