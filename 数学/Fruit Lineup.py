MOD = 998244353

def prepare(n, MOD):
    """预处理阶乘和逆元"""
    f = 1
    for m in range(1, n + 1):
        f = f * m % MOD
    fn = f  # n!
    inv = pow(f, MOD - 2, MOD)  # n!的逆元
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv = inv * m % MOD
        invs[m - 1] = inv
    return fn, invs

A, B, C, D = map(int, input().split())
N = A + B + C + D

# 预处理阶乘和逆元数组
frac = [1] * (N + 1)
fn, invs = prepare(N, MOD)  # 注意这里参数为N，处理到N!的逆元
for i in range(1, N + 1):
    frac[i] = frac[i - 1] * i % MOD

def comb(a, b):
    """计算组合数C(a, b) mod MOD"""
    if a < 0 or b < 0 or a < b:
        return 0
    return frac[a] * invs[b] % MOD * invs[a - b] % MOD

ans = 0
# i的取值范围应为A到min(A+B, N-C)
max_i = min(A + B, N - C)
for i in range(A, max_i + 1):
    if (i - A) > B or (N - i - C) > D:
        continue  # 确保B和D的数量足够
    # 前i-1个位置选A-1个A类，剩下的i-A个是B类
    front = comb(i - 1, A - 1)
    # 后N-i个位置选C个C类，剩下的D类
    back = comb(N - i, C)
    ans = (ans + front * back) % MOD

print(ans)