import json
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # solution: sort and merge
        sorted_intervals = sorted(intervals)
        if len(intervals) <= 1:
            return intervals
        result = []
        point = sorted_intervals[0]
        for interval in sorted_intervals[1:]:
            if interval[0] <= point[1] and interval[1] > point[1]:
                point[1] = interval[1]
            elif interval[0] > point[1]:
                result.append(point)
                point = interval
        result.append(point)
        return result
        

def stringToInt2dArray(input):
    return json.loads(input)

def int2dArrayToString(input):
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
            intervals = stringToInt2dArray(line)
            
            ret = Solution().merge(intervals)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()