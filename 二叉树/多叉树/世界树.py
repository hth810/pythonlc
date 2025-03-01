n = int(input())
children = [[] for _ in range(n + 1)]
flowers = [0] * (n + 1)

def dfs(u):
    if len(children[u]) == 0:
        return
    for child in children[u]:
        flowers[child] += 1
        dfs(child)


for i in range(n):
    op, u = map(int, input().split())
    if op == 1:
        children[u].append(i + 2)
    elif op == 2:
        flowers[u] += 1
        dfs(u)

for i in range(1, n + 1):
    if flowers[i] !=0:
        print(flowers[i],end=' ')