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
    primes(200)


def primes(n):
    o = range(2, n+1 )

    for i in o :
        d = range(2, i/2+1 )
        isflag = 1
        for j in d :
            if (i%j==0):
                isflag = 0
        if (isflag==1):
            print(i)
    print


def RingOut( n, m ):
    mans = []
    for i in range(n):
        mans += [i+1]

    print len(mans)


    c = 0
    j = 0
    while len(mans) > 0:
        c+=1
        if ( c==m ):
           c=0
           print mans[j],
           mans.remove( mans[j])
        j+=1
        if j>=len(mans):
           j=0

    print

if __name__ == '__main__':
    main()