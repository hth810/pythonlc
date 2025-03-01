class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        big=self.calculate(nums2)
        bigMap={}
        for i in range(len(nums2)):
            bigMap[nums2[i]]=big[i]
        ans=[0]*len(nums1)
        for i in range(len(nums1)):
            ans[i]=bigMap[nums1[i]]

        return ans

    def calculate(self,nums2):
        n=len(nums2)
        res=[0]*n
        s=[]
        for i in range(n-1,-1,-1):
            while s and s[-1]<=nums2[i]:
                s.pop()
            res[i]= -1 if not s else s[-1]
            s.append(nums2[i])

        return res

