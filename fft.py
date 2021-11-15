#################
# FAST FOURIER TRANSFORM
# A python script to compute fast fourier transform of a sequence
#
# #######

# Dependencies
import numpy as np
import matplotlib.pyplot as plt

# helper library...
from src.helpers import *


def fft(coeff):
    '''
      function to compute fast fourier transform of the input sequence 
    '''
    N:int = len(coeff) # length of the input sequence

    # base case for the recursion return F(1)
    if(N == 1):
        return [cpxnum(coeff[0], 0)]

    # round N to next perfect power of 2
    N = int(pow(2, np.ceil(np.log2(N))))
    # and increase the length of sequence by padding zeros
    n = N-len(coeff)
    for i in range(n):
        coeff.append(0)

    # w = e^((2*pi*i)/n)
    # nth roots of unity given by...
    # w^j = e^((2*pi*i*j)/n) for j: 0 -> n-1

    # saperate even and odd terms from the input sequence 
    Pe = []
    Po = []
    for i in range(N):
        Po.append(coeff[i]) if i&1 else Pe.append(coeff[i])

    # recursion
    (ye, yo) = (fft(Pe), fft(Po))

    # initialize output list and compute the result
    y = [cpxnum(0,0)]*N
    for i in range(N//2):
        wi =  cpxnum(np.cos( (2*np.pi*i)/N ), np.sin( (2*np.pi*i)/N))
        y[i] = ye[i].add(yo[i].mul(wi))
        y[i + N//2] = ye[i].sub(yo[i].mul(wi))

    return y
    

def main():
    '''
        driver code
    '''
    # get input sequence
    t = [i for i in range(100)]
    coeff = [np.sin(2*np.pi*i/10) for i in t]

    # compute fft and plot it!
    value = fft(coeff)
    rvalue = [elem.real for elem in value]  # real part of the fft

    plt.plot(coeff)
    plt.plot(rvalue)
    plt.show()



if __name__ == '__main__':
    main()
