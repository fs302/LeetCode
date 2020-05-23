import json
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        # solution: 1-find start position & 2-handle overlap
        if len(intervals) == 0:
            intervals.append(newInterval)
        else:
            left, right = 0, len(intervals)-1
            while left <= right:
                mid = (left + right)/2
                if intervals[mid][0] < newInterval[0]:
                    left = mid+1
                else:
                    right = mid-1
            mid = (left + right)/2
            intervals.insert(mid+1,newInterval)
            # print(left, mid, right,intervals)
        if len(intervals) <= 1:
            return intervals
        result = []
        point = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= point[1] and interval[1] > point[1]:
                point[1] = interval[1]
            elif interval[0] > point[1]:
                result.append(point)
                point = interval
        result.append(point)
        return result
        

def stringToInt2dArray(input):
    return json.loads(input)

def stringToIntegerList(input):
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
            line = lines.next()
            newInterval = stringToIntegerList(line)
            
            ret = Solution().insert(intervals, newInterval)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()