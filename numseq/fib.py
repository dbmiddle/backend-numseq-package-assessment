def fib(n):
    '''Compute the nth term of fibonacci sequence'''
    fib_seq = [0, 1]
    for i in range(2, n+1):
        fib_seq.append(fib_seq[i - 2] + fib_seq[i - 1])
    return fib_seq[n]