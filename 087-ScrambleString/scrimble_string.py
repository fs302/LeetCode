from collections import Counter

class Solution:
    def __init__(self):
        self.memory = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        # naive-solution
        ## first-rule: digit distribution match
        ## second-rule: can it be transformed into several small problems

        # better-one, memorized search
        
        if s1 == s2:
            return True
        
        if Counter(s1) != Counter(s2):
            return False

        pair = s1+'_'+s2
        if pair in self.memory:
            return self.memory[pair]
        reverse_pair = s2+'_'+s1
        if reverse_pair in self.memory:
            return self.memory[reverse_pair]

        l = len(s1)
        for i in range(1,l):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                self.memory[pair] = True
                return True
            if self.isScramble(s1[:i],s2[l-i:]) and self.isScramble(s1[i:],s2[:l-i]):
                self.memory[pair] = True
                return True
        
        self.memory[pair] = False
        return False
def main():
    s1 = "eebaacbcbcadaaedceaaacadccd"
    s2 = "eadcaacabaddaceacbceaabeccd"
    s = Solution()
    print(s1, s2, s.isScramble(s1, s2))

    s1 = "rgeat"
    s2 = "great"
    print(s1, s2, s.isScramble(s1, s2))


if __name__ == '__main__':
    main()