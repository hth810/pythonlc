class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)
        max_possible_length = len_s + len_t

        for l in range(max_possible_length, 0, -1):
            s_min = max(0, l - len_t)
            s_max = min(len_s, l)
            for s_sub_len in range(s_min, s_max + 1):
                t_sub_len = l - s_sub_len
                if t_sub_len < 0 or t_sub_len > len_t:
                    continue
                for i in range(len_s - s_sub_len + 1):
                    s_sub = s[i:i + s_sub_len]
                    for j in range(len_t - t_sub_len + 1):
                        t_sub = t[j:j + t_sub_len]
                        candidate = s_sub + t_sub
                        if candidate == candidate[::-1]:
                            return l
        return 1