from functools import cache


def guoHe(deadpoint,m,n):
    @cache
    def dfs(i,j):
        if i<0 or j<0:
            return 0
        if i==0 and j==0:
            return 1
        if [i,j] in deadpoint:
            return 0
        return dfs(i-1,j)+dfs(i,j-1)

    return dfs(m,n)

m,n,a,b=map(int,input().split())
deadpoint=[[a-2,b-1],[a-1,b-2],[a-2,b+1],[a-1,b+2],[a+2,b-1],[a+1,b-2],[a+2,b+1],[a+1,b+2],[a,b]]
res=guoHe(deadpoint,m,n)
print(res)