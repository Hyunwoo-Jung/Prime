import math # 제곱근을 구할 때 사용할 수학 모듈

def is_prime(n):
    if n<=1:
        return False # 1 이하는 소수가 아니므로 False
    for i in range(2, int(math.sqrt(n)) + 1): # math.sqrt(n) -> 제곱근을 계산
        if n % i == 0: # 나누어떨어지는지 판정 
            return False # 나누어떨어지면 False
    return True # 어떠한 숫자로도 나누어떨어지지 않으면 True