from bisect import bisect_right


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        n=len(words)
        fre=[0]*len(words)
        for i in range(len(words)):
            temp=sorted(words[i])
            fre[i]=temp.count(temp[0])
        fre.sort()
        res=[]
        for j in queries:
            a=sorted(j).count(sorted(j)[0])
            pos=bisect_right(fre,a)
            res.append(n-pos)
        return res

