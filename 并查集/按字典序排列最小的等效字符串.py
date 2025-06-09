from string import ascii_lowercase


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        pa={c:c for c in ascii_lowercase}
        def find(x):
            if pa[x]!=x:
                pa[x]=find(pa[x])
            return pa[x]
        def merge(i,j):
            small,big=sorted((find(i),find(j)))
            pa[big]=small
        for i,j in zip(s1,s2):
            merge(i,j)

        return ''.join(find(x) for x in baseStr)