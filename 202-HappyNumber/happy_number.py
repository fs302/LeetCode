# 递归法
'''
class Solution:
    def __init__(self):
        self.memory = []
    
    def sum_of_square(self, n: int) -> int:
        s = 0
        while n > 0:
            digit = n % 10
            s += digit * digit 
            n = int(n / 10)
        return s
    
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n in self.memory:
            return False
        self.memory.append(n)
        next_n = self.sum_of_square(n)
        return self.isHappy(next_n)
'''
# 循环数组
class Solution:
    def sum_of_square(self, n: int) -> int:
        s = 0
        while n > 0:
            digit = n % 10
            s += digit * digit 
            n = int(n / 10)
        return s
    
    def isHappy(self, n: int) -> bool:
        memory = []
        next_n = self.sum_of_square(n)
        while next_n != 1:
            if next_n in memory:
                return False 
            memory.append(next_n)
            next_n = self.sum_of_square(next_n)
        return True