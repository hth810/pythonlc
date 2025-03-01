class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        result=[0]*len(queries)
        for i in range(len(queries)):
            left, right =queries[i][0], queries[i][0]
            one, zero=0,0
            res=0
            while right<queries[i][1]+1:
                if s[right]=='1':
                    one+=1
                else:
                    zero+=1
                while one>k and zero>k and left<=right:
                    if s[left]=='1':
                        one-=1
                    else:
                        zero-=1
                    left+=1
                res+=right-left+1
                right+=1
            result[i]=res
        return result