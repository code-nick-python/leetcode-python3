class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        import re
        result=re.search(needle,haystack)
        try:
            result=result.span()[0]
            return result
        except:
            return -1
