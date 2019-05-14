class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        pattern=re.compile(p)
        result=pattern.search(s)
        if result:
            if len(s)==len(result.group()):
                return True
        return False
