class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        s=0
        a=0
        temp=0
        for i in range(n):
            if grumpy[i]!=1:
                s+=customers[i]
        for i,c in enumerate(customers):
            if grumpy[i]==1:
                temp+=c
            if i<minutes-1:
                continue
            a=max(a,temp)
            if grumpy[i-minutes+1]==1:
                temp-=customers[i-minutes+1]
        return s+a
