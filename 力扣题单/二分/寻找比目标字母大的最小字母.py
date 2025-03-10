class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n=len(letters)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if letters[mid]<=target:
                left+=1
            else:
                right-=1

        return letters[left] if left<n else letters[0]
