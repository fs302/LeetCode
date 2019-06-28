import json
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = {'2':['a','b','c'],
                     '3':['d','e','f'],
                     '4':['g','h','i'],
                     '5':['j','k','l'],
                     '6':['m','n','o'],
                     '7':['p','q','r','s'],
                     '8':['t','u','v'],
                     '9':['w','x','y','z']
                    }
        if len(digits)==0:
            return []
        outputs = ['']
        for digit in digits:
            new_outputs = []
            for item in outputs:
                for value in digit_map[digit]:
                    new_outputs.append(item+value)
            outputs = new_outputs
        return outputs

def stringToString(input):
    return input.decode('string_escape')

def stringArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            digits = stringToString(line)
            
            ret = Solution().letterCombinations(digits)

            out = stringArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()