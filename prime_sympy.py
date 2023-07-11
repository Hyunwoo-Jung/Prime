from sympy import sieve, isprime

# 주어진 범위 소수 구하기
print([i for i in sieve.primerange(1,200)])

# 주어진 수가 소수인지 판정
print(isprime(101))