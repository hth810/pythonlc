class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans=0
        temp=0
        for i,c in enumerate(arr):
            temp+=c
            if i<k-1:
                continue
            if (temp/k)>=threshold:
                ans+=1
            temp-=arr[i-k+1]

        return ans