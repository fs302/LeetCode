import json

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        results = []
        if len(s)==0 or len(words)==0:
            return results
        
        word_len = len(words[0])
        window_len = word_len*len(words)
        s_len = len(s)
        
        for i in range(s_len-window_len+1):
            substring = s[i:i+window_len]
            check_list = words[:]
            for k in range(0,window_len,word_len):
                w = substring[k:k+word_len]
                if w in check_list:
                    check_list.remove(w)
                else:
                    break
            if len(check_list) == 0:
                results.append(i)
                
        return results

def stringToString(input):
    return input[1:-1].decode('string_escape')

def stringToStringArray(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            words = stringToStringArray(line)
            
            ret = Solution().findSubstring(s, words)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()