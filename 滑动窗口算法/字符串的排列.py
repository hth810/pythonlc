class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        has,want={},{}
        for c in s1:
            has[c]=has.get(c,0)+1
        left,right,valid=0,0,0
        while right<len(s2):
            c=s2[right]
            right+=1
            if c in has:
                want[c]=want.get(c,0)+1
                if want[c]==has[c]:
                    valid+=1
            while right-left>=len(s1):
                if valid==len(has):
                    return True
                d=s2[left]
                left+=1
                if d in has:
                    if want[d]==has[d]:
                        valid-=1
                    want[d]-=1
        return False
