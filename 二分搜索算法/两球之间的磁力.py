class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def judge(mid):
            cnt=1
            pos=position[0]
            for i in range(1,len(position)):
                if position[i]-pos>=mid:
                    cnt+=1
                    pos=position[i]
            return cnt>=m
        position.sort()
        left=-1
        right=max(position)+1
        while left+1<right:
            mid=(left+right)//2
            if judge(mid):
                left=mid
            else:
                right=mid
        return left