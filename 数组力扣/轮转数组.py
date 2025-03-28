class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i,j):
            if i>=j:
                return
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
            reverse(i,j)
        n=len(nums)
        k%=n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        """
        Do not return anything, modify nums in-place instead.
        """
