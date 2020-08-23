import re
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        clean_path = re.sub('[/]+','/',path)
        items = clean_path[1:].split('/')
        dirs = []
        for item in items:
            if item in ['..']:
                if len(dirs) > 0:
                    dirs.pop()
            elif item == '.':
                continue
            else:
                if len(item) > 0:
                    dirs.append(item)
        new_path = '/'+'/'.join(dirs)
        return new_path
        
def main():
    #path = '/a//b////c/d//././/..'
    # path = '/home//foo/'
    path = '/../'
    ret = Solution().simplifyPath(path)
    print(ret)

if __name__ == '__main__':
    main()       