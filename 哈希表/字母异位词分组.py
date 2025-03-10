from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt=defaultdict(list)
        for i in strs:
            cnt[''.join(sorted(i))].append(i)
        return list(cnt.values())
