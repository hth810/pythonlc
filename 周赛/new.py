from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def main(words, k):
    n = len(words)
    answer = [0] * n
    count = defaultdict(int)
    for word in words:
        count[word] += 1

    # 构建Trie树并统计每个节点的count（不同字符串的数量）
    trie = TrieNode()
    word_set = set(words)
    for s in word_set:
        node = trie
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += 1

    # 预处理每个字符串的贡献
    # 这里记录每个字符串的所有前缀节点，以便后续快速更新
    prefix_nodes = defaultdict(list)
    for s in set(words):
        node = trie
        nodes = []
        for c in s:
            node = node.children[c]
            nodes.append(node)
        prefix_nodes[s] = nodes

    # 预处理每个字符串的出现次数
    original_count = defaultdict(int)
    for word in words:
        original_count[word] += 1

    for i in range(n):
        s_i = words[i]
        remaining = n - 1
        if remaining < k:
            answer[i] = 0
            continue

        # 处理情况a: 出现次数 >=k 的最长字符串的长度
        # 计算移除后的出现次数
        new_count_i = original_count[s_i] - 1
        a_candidate = len(s_i) if new_count_i >= k else 0

        # 处理情况b: 不同字符串的最长公共前缀
        # 先暂时移除s_i的影响
        # 如果s_i在word_set中，则在Trie中减少其所有前缀节点的count
        if s_i in word_set:
            for node in prefix_nodes[s_i]:
                node.count -= 1

        # 在Trie中查找最深的节点，其count >=k
        max_prefix = 0
        stack = [(trie, 0)]
        while stack:
            node, depth = stack.pop()
            if depth > max_prefix and node.count >= k:
                max_prefix = depth
            for c, child in node.children.items():
                stack.append((child, depth + 1))
        b_candidate = max_prefix

        # 恢复s_i的影响
        if s_i in word_set:
            for node in prefix_nodes[s_i]:
                node.count += 1

        # 计算最终候选值
        current_candidate = max(a_candidate, b_candidate)
        answer[i] = current_candidate if current_candidate != 0 else 0

    return answer

# 示例测试
words1 = ["jump","run","run","jump","run"]
k1 = 2
print(main(words1, k1))  # 期望输出 [3,4,4,3,4]

words2 = ["dog","racer","car"]
k2 = 2
print(main(words2, k2))  # 期望输出 [0,0,0]