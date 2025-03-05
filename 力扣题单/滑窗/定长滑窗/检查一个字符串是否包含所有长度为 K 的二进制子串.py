class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=len(s)
        if k>n:
            return False
        need=pow(2,k)
        if n-k+1<need:
            return False
        w={}
        temp=''
        for i,c in enumerate(s):
            temp+=c
            if i<k-1:
                continue
            w[temp]=w.get(temp,0)+1
            temp=temp[1:]
        return len(w)==need
