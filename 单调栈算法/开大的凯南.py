t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    stack = []
    for num in nums:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    print("YES" if stack==sorted(stack) else "NO")