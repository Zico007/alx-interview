def minOperations(n):
    if n == 1:
        return 0
    
    ops = 0

    # We'll try to break n down by its smallest prime factors.
    # This is similar to the strategy of copy-pasting the largest chunk possible.
    for i in range(2, n + 1):
        while n % i == 0:
            ops += i
            n //= i

    return ops
