class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        n, m = len(s), len(p)
        f = [[False for j in range(m+1)] for i in range(n+1)]
        f[0][0] = True
        for j in range(1,m+1):
            if p[j-1] == '*':
                f[0][j] = f[0][j-1]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1] == p[j-1] or p[j-1] == '?': # jump:s-1&p-1
                    f[i][j] = f[i-1][j-1]
                elif p[j-1] == '*':
                    f[i][j] = max(f[i-1][j],f[i][j-1]) # jump1:s-1,jump2:p-1
        return f[-1][-1]

def stringToString(input):
    import json
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            line = next(lines)
            p = stringToString(line);
            
            ret = Solution().isMatch(s, p)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()