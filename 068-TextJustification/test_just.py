class Solution(object):
    
    def calLineLength(self, arr):
        return len(arr) - 1 + sum([len(st) for st in arr])
        
    def formatLine(self, arr, maxWidth):
        
        if len(arr) == 1:
            return arr[0]+' '*(maxWidth-len(arr[0]))
        
        words_len = sum([len(st) for st in arr])
        space_cnt = len(arr) - 1
        space = int((maxWidth - words_len)/space_cnt)
        extra_gift = maxWidth - words_len - space*space_cnt
        nice_line = ''
        for word in arr[:-1]:
            nice_line = nice_line + word + ' '*space
            if extra_gift > 0:
                nice_line += ' '
                extra_gift -= 1
        nice_line += arr[-1]
        return nice_line
        
        
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        l = len(words)
        i = 0
        results = []
        tmp_queue = []
        while i < l:
            tmp_queue.append(words[i])
            if self.calLineLength(tmp_queue) > maxWidth:
                tmp_queue.pop()
                results.append(self.formatLine(tmp_queue, maxWidth))
                tmp_queue = [words[i]]
            i += 1
        
        # handle the last line
        if len(tmp_queue) > 0:
            line = ' '.join(tmp_queue)
            line = line + ' '*(maxWidth-len(line))
            results.append(line)
        
        return results

def main():
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer","Art","is","everything","else","we","do"]
    maxWidth = 20
    ret = Solution().fullJustify(words, maxWidth)
    print(ret)

if __name__ == '__main__':
    main()                