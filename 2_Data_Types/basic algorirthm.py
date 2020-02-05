#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      abeliu
#
# Created:     09/09/2014
# Copyright:   (c) abeliu 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    multiplication_table()

"""--------------------------------------
Function primes
print all the primes between 2~n
--------------------------------------"""
def primes(n):
    o = range(2, n+1 )

    for i in o :
        d = range(2, i/2+1 )
        isflag = 1
        for j in d :
            if (i%j==0):
                isflag = 0
        if (isflag==1):
            print(i, sep=' ')
    print


"""--------------------------------------
Function ring_out
print all the numbers in the order of pick 
out of the ring. ring size is n, pick out 
a number every m elements.
--------------------------------------"""
def ring_out( n, m ):
    mans = []
    for i in range(n):
        mans += [i+1]

    print(len(mans))

    c = 0
    j = 0
    while len(mans) > 0:
        c+=1
        if ( c==m ):
           c=0
           print( mans[j], end=' ')
           mans.remove( mans[j])
        else:
            j+=1   
        if j>=len(mans):
           j=0

    print()

"""--------------------------------------
Function multiplication table
print multiplication table
tips:
1. range(start,stop, step), last element < stop
2. print format string: %d, %2d, %-2d
--------------------------------------"""
def multiplication_table():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d=%-2d"%(j,i,i*j), end='\t')
        print()


if __name__ == '__main__':
    main()
