'''
任意 k 个 -> 连续 k 个
1. 排序，那么只需要考虑长为 k 的连续子数组的 LCP
2. 排序后，子数组的 LCP = LCP(第一个字符串，最后一个字符串)
把 k 个字符串的问题转换成 2 个字符串的问题
3. 如果不删除，那么答案是多少？
暴力枚举所有长为 k 的子数组，根据（2），
计算所有的 LCP(words[i], words[i+k-1])，取最大值，即为不删除时的答案
4. 记录最大的 LCP 对应的子数组是 [mx_i, mx_i+k-1]
记录次大的 LCP 对应的子数组是 [mx2_i, mx2_i+k-1]
5. 考虑删除一个字符串
分类讨论：
a. 如果删除的字符串不在 [mx_i, mx_i+k-1] 中，那么答案就是不删除时的，即最大 LCP
剩下的问题就是删除在 [mx_i, mx_i+k-1] 中的字符串
b. 如果删除的字符串不在 [mx2_i, mx2_i+k-1] 中，那么答案就是次大的 LCP
c. 如果删除的字符串即在 [mx_i, mx_i+k-1] 中，又在 [mx2_i, mx2_i+k-1] 中，那么答案是多少？
意味着这两个数组是重叠的，重叠的字符串（也是我们删除的字符串 s）即有最大 LCP 又有次大 LCP
围绕重叠的字符串讨论，那么次大 LCP 也是最大 LCP 的前缀
去掉字符串 s，可以再加一个交集中的其他字符串进来，仍然是 k 个字符串，且次大LCP是不变的
那么答案就是次大的 LCP
'''
class Solution:
    def Lcp(self,s,t):
        for i,(x,y) in enumerate(zip(s,t)):
            if x!=y:
                return i
        return min(len(s),len(t))
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n=len(words)
        if k>=n:
            return [0]*n

        idx=list(range(n))
        idx.sort(key=lambda x:words[x])

        mx=mx2=mx_i=-1
        for i in range(n-k+1):
            lcp=self.Lcp(words[idx[i]],words[idx[i+k-1]])
            if lcp>mx:
                mx,mx2,mx_i=lcp,mx,i
            elif lcp>mx2:
                mx2=lcp

        ans=[mx]*n
        for i in idx[mx_i:mx_i+k]:
            ans[i]=mx2
        return ans