from scipy.special import binom as binomial

def bernouilli_gen(init=1):
    """generator of Bernouilli numbers
    :param init: int -1 or +1. 
    * -1 for "first Bernoulli numbers" with B1=-1/2
    * +1 for "second Bernoulli numbers" with B1=+1/2
    https://en.wikipedia.org/wiki/Bernoulli_number
    https://rosettacode.org/wiki/Bernoulli_numbers#Python:_Optimised_task_algorithm
    """
    from fractions import Fraction
    B, m = [], 0
    while True:
        B.append(Fraction(1, m+1))
        for j in range(m, 0, -1):
            B[j-1] = j*(B[j-1] - B[j])
        yield init*B[0] if m==1 else B[0]# (which is Bm)
        m += 1
            
def faulhaber(n,p):
    """ sum of the p-th powers of the first n positive integers
    :return: 1^p + 2^p + 3^p + ... + n^p
    https://en.wikipedia.org/wiki/Faulhaber%27s_formula
    """
    s=0
    for j,a in enumerate(bernouilli_gen()):
        if j>p : break
        s=s+binomial(p+1,j)*a*n**(p+1-j)
    return s//(p+1)