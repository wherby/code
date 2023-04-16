# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c9607c/0000000000cad13d
# https://www.youtube.com/watch?v=JTC3LVy2uTI&ab_channel=NealWu
# algorithm/mathA/extendedEuclid/pdf/extendedEuclid.pdf


 
def modInverse(a, m):
    g = m 
    r = a 
    x,y = 0,1
    
    while r !=0:
        q = g //r 
        g = g %r 
        g,r = r,g 
        x -= q *y 
        x,y = y,x
    return x if x>0 else x+m
 
 
# Driver code
if __name__ == "__main__":
    A = 3
    M = 11
 
    # Function call
    print("Modular multiplicative inverse is",
          modInverse(A, M))
 
# This code is contributed by Nikita tiwari.
#print(modInverse(1432,123211))