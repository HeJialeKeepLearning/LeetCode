class Solution:
    def nthSuperUglyNumber(self, n: int, primes):
        prime_dict = {}
        for each_prime in primes:
            prime_dict[each_prime] = 0
        dp = [0] * n
        dp[0] = 1
        for index in range(1, n):
            dp[index] = min([prime * dp[prime_dict[prime]] for prime in primes])
            for prime in primes:
                if dp[index] == prime * dp[prime_dict[prime]]:
                    prime_dict[prime] += 1
        return dp[-1]
