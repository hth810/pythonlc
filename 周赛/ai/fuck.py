import heapq
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n=len(nums1)
        ans=[0]*n
        pairs=sorted(zip(nums1,nums2,range(n)),key=lambda x:x[0])
        group=[]
        cur_a=None
        cur_g=[]
        for a,b,idx in pairs:
            if a!=cur_a:
                if cur_a!=None:
                    group.append(cur_g)
                cur_a=a
                cur_g=[]
            cur_g.append((b,idx))
        if cur_g:
            group.append(cur_g)
        heap=[]
        sum_k=0
        for g in group:
            for b,idx in g:
                ans[idx]=sum_k
            b_vals=[b for b,idx in g]
            b_vals.sort(reverse=True)
            for v in b_vals:
                if len(heap)<k:
                    heapq.heappush(heap,v)
                    sum_k+=v
                else:
                    if v>heap[0]:
                        sum_k-=heapq.heappop(heap)
                        heapq.heappush(heap,v)
                        sum_k+=v
        return ans