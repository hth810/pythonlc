from collections import defaultdict


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n=len(cards)
        ans=float('inf')
        cnt=defaultdict(lambda :-1)
        for i,c in enumerate(cards):
            if cnt[c]!=-1:
                ans=min(ans,i-cnt[c]+1)
                cnt[c]=i
            else:
                cnt[c]=i
        return ans if ans!=float('inf') else -1