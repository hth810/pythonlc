from functools import cache


class Solution:
    def __init__(self):
        self.res=[]
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        track=""
        @cache
        def traverse(digits,track,i):
            if len(track)==len(digits):
                self.res.append(track)
                return
            if i>=len(digits):
                return
            for j in phone[digits[i]]:
                traverse(digits,track+j,i+1)

        traverse(digits,track,0)
        return self.res