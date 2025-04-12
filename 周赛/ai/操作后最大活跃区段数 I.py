class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        original_ones = s.count('1')
        t = '1' + s + '1'

        blocks = []
        n = len(t)
        if n == 0:
            return original_ones
        current_char = t[0]
        start = 0
        for i in range(1, n):
            if t[i] != current_char:
                blocks.append({'type': current_char, 'length': i - start})
                current_char = t[i]
                start = i
        blocks.append({'type': current_char, 'length': n - start})

        max_value = 0
        n_blocks = len(blocks)
        for i in range(n_blocks):
            if blocks[i]['type'] == '1':
                if i >= 1 and (i + 1) < n_blocks and blocks[i - 1]['type'] == '0' and blocks[i + 1]['type'] == '0':
                    if (i - 2 >= 0) and (i + 2 < n_blocks) and blocks[i - 2]['type'] == '1' and blocks[i + 2][
                        'type'] == '1':
                        a = blocks[i - 1]['length']
                        b = blocks[i + 1]['length']
                        current_sum = a + b
                        if current_sum > max_value:
                            max_value = current_sum
        return original_ones + max_value