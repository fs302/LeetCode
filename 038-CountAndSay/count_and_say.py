class Solution(object):
    def say(self, state):
        new_state = ""   
        digit = state[0]
        i = 1
        cnt = 1
        while i < len(state):
            if state[i] == state[i-1]:
                cnt += 1
            else:
                new_state = new_state + str(cnt) + digit
                digit = state[i]
                cnt = 1
            i += 1
        new_state = new_state + str(cnt) + digit
        return new_state
        
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        state = "1"
        for i in range(n-1):
            state = self.say(state)
            # print(state)
        return state

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
            n = stringToInt(line)
            
            ret = Solution().countAndSay(n)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()