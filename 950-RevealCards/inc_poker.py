import json

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        ordered_deck = sorted(deck,reverse=True)
        res = []
        for item in ordered_deck:
            if len(res) > 0:
                v = res.pop(0)
                res.append(v)
            res.append(item)
        return res[::-1]

def stringToIntegerList(input):
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
            deck = stringToIntegerList(line)
            
            ret = Solution().deckRevealedIncreasing(deck)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()