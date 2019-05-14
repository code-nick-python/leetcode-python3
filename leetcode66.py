class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        middle=""
        result=[]
        for i in digits:
            middle += str(i)
        middle = int(middle) + 1
        for i in str(middle):
            result.append(int(i))
        return result
