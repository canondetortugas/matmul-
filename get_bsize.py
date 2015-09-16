#!/share/apps/python/anaconda/bin/python

import sys

lmin = 2
lmax = 4

lrange = range(lmin,lmax+1)

range_p = [2**l for l in lrange]

sizes = []

for r in range_p:
    sizes = sizes+[r-1, r, r+1]


if __name__=='__main__':
    if len(sys.argv) == 2:
        print sizes[int(sys.argv[1])-1]
    else:
        print len(sizes)
