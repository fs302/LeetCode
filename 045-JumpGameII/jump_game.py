import json
class Solution:
    def jump(self, nums):
        n = len(nums)
        f = [n for i in range(n)]
        f[n-1] = 0
        for p in range(2,n+1):
            i = n - p
            # print(f[i+1:i+nums[i]+1])
            f[i] = min(f[i+1:i+nums[i]+1]) + 1
        return f[0]

def stringToIntegerList(input):
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
            nums = stringToIntegerList(line);
            
            ret = Solution().jump(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()