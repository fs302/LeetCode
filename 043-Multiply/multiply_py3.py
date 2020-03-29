class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sum_arr = []
        ln1,ln2 = len(num1),len(num2)
        for i in range(ln1):
            digit_a = int(num1[ln1-i-1])
            p = i
            for j in range(ln2):
                digit_b = int(num2[ln2-j-1])
                while len(sum_arr)-1 < p:
                    sum_arr.append(0)
                sum_arr[p] += digit_a * digit_b
                p += 1
        i = 0
        while i < len(sum_arr):
            if sum_arr[i] >= 10:
                tmp = sum_arr[i]
                sum_arr[i] = tmp % 10
                if len(sum_arr)-1 < i+1:
                    sum_arr.append(0)
                sum_arr[i+1] += int(tmp / 10)
            i += 1
        # print(sum_arr)
        result = ""
        i = len(sum_arr)-1
        while sum_arr[i] == 0 and i >= 0: # filter extra-zeros
            i -= 1
        while i >= 0:
            result += str(sum_arr[i])
            i -= 1
        if len(result) == 0:
            result = "0"
        return result
            

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
            num1 = stringToString(line);
            line = next(lines)
            num2 = stringToString(line);
            
            ret = Solution().multiply(num1, num2)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()