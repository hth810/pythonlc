# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         result=[0]*26
#         for i in s:
#             result[ord(i)-97]+=1
#         for i in t:
#             result[ord(i)-97]-=1
#         for i in result:
#             if i!=0:
#                 return False
#         return True
#优解1
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s)==sorted(t)
#优解2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s)==Counter(t)