# 生成小于等于n的所有质数 (埃拉托斯特尼筛法)
def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2,n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i,n+1,i):  # 从i**2开始遍历是因为在i**2之前的所有小于i**2的倍数已经在前面处理过了
                is_prime[j] = False  # 把所有i的倍数标记为合数
    return primes,is_prime  # 返回 2->n 的质数数组及布尔数组