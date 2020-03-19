def primes(n):
    '''Return a list of prime numbers less than n'''
    primes_to_n = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes_to_n.append(i)
    return primes_to_n


def is_prime(m):
    '''Return boolean indicating if m is a prime number'''
    # Corner cases
    if (m <= 1):
        return False
    if (m <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (m % 2 == 0 or m % 3 == 0):
        return False
    i = 5
    while(i * i <= m):
        if (m % i == 0 or m % (i + 2) == 0):
            return False
        i = i + 6

    return True
