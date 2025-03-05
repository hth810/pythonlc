class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp=code+code
        res=[]
        cnt=0
        n=len(code)
        if k==0:
            return [0]*len(code)
        if k>0:
            t=temp[1:k-n]
            for i,c in enumerate(t):
                cnt+=c
                if i<k-1:
                    continue
                res.append(cnt)
                cnt-=t[i-k+1]
            return res

        if k<0:
            k=abs(k)
            t=temp[::-1]
            t=t[1:k-n]
            for i,c in enumerate(t):
                cnt+=c
                if i<k-1:
                    continue
                res.append(cnt)
                cnt-=t[i-k+1]

            return res[::-1]


