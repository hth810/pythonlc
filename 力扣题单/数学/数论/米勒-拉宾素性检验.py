def is_prime_miller_rabin(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in bases:
        if a >= n:
            continue  # 跳过超过 n 的基底
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue  # 通过当前基底测试
        composite = True
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                composite = False  # 发现 n-1，退出循环
                break
        if composite:
            return False  # 确定是合数
    return True  # 通过所有基底测试，是质数

print(is_prime_miller_rabin(97))  # 输出 True