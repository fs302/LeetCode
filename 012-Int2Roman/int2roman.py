class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        constant_symbol = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        base_symbol = {1:'I',5:'I',10:'I',50:'X',100:'X',500:'C',1000:'C'}
        symbols = [1000,500,100,50,10,5,1]
        sub_symbols = [4000,900,400,90,40,9,4,0]
        raw_result = ''
        while (num>0):
            for i in range(len(symbols)):
                if num >= symbols[i] :
                    if num < sub_symbols[i]:
                        v = symbols[i]
                        num -= v
                        raw_result += constant_symbol[v]
                    else:
                        father = symbols[i-1]
                        raw_result += (base_symbol[father]+constant_symbol[father])
                        num -= sub_symbols[i]
                    break
        
        return raw_result
        

def stringToInt(input):
    return int(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            num = stringToInt(line)
            
            ret = Solution().intToRoman(num)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()