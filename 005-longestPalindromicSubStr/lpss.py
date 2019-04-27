class Solution(object):
    def checkPalind(self, substr):
        if len(substr) <= 1:
            return True
        l = len(substr)
        res = substr[:int(l/2)]==substr[::-1][:int(l/2)]
        return res 
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur_palindrome = ''
        palindrome = []
        best = ''
        for i in range(len(s)):
            if (i-len(cur_palindrome)-1 >= 0 and s[i]==s[i-len(cur_palindrome)-1]):
                cur_palindrome = s[i-len(cur_palindrome)-1] + cur_palindrome + s[i] # case-1: padding two sides
            else:
                while len(cur_palindrome) > 0 and not (self.checkPalind(cur_palindrome+s[i])):
                    cur_palindrome = cur_palindrome[1:]                             # case-2: leaving head
                cur_palindrome += s[i]
            if len(cur_palindrome) >= len(best):
                best = cur_palindrome
        return best

if __name__=='__main__':
    s = Solution()
    input_str = ['babad','cbbd','aaaa','a','aaa','abcdefgfe','bananas','aaabaaaa']
    for st in input_str:
        print st,'->longestPalindrome:',s.longestPalindrome(st)