class Solution:
    def plusOne(self, digits):
        if digits is None or len(digits) == 0:
            return [1]
        digits[-1] += 1
        i = len(digits) - 1
        # from the bottom pos
        while digits[i] >= 10 and i > 0:
            digits[i-1] += 1
            digits[i] -= 10
            i -= 1
        # handle overflow
        if digits[0] >= 10:
            digits[0] -= 10
            digits.insert(0,1)

        ## Another solution: convert to string then int, and add as Integer
        return digits

if __name__ == '__main__':
    s = Solution()
    _input = []
    res = s.plusOne(_input)
    print(res)