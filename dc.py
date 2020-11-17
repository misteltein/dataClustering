import numpy as np
import matplotlib.pyplot as plt

EPS   = 1.0e-10
EPS_2 = 1.0e-6
xi    = # WRITE_YOUR_PARAMETER_HERE
numPoints = 10

P = np.loadtxt( "sampleA.csv", delimiter=',', skiprows=1)

def norm2( a, b ):
    # Vectors a, b |-> Scalar
    # Return the squared distance between a and b
    # Your code here

def g( a, b ):
    # Vectors a, b |-> Scalar
    # Your code here

def next( x_t ):
    # Vector x_t |-> Vector
    # Your code here

def x_r( x0 ):
    # Vector x0 |-> Vector
    # Your code here

rP = [ x_r( pi ) for pi in P[ 0 : numPoints ] ]

unique = []
for r in rP:
    collection = True
    for u in unique:
        if norm2( r, u ) < EPS_2:
            collection = False
            break
    if collection:
        unique.append( r )

#for i, u in enumerate(unique):
#    print('cluster #'+str(i+1), u)

def Id( x ):
    for i, r in enumerate( unique ):
        if norm2( x, r ) < EPS_2 :
            return i;
    return -1;

clusterId = [ Id( rpi ) for rpi in rP ]

def color( c ):
    cs = 'rgbcmyk'
    return cs[ c % 7 ]

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.scatter( P[:,0], P[:,1], c='gray', alpha=0.05, s=1 )
ax.scatter( [ p[0] for p in P[ 0 : numPoints ] ], [ p[1] for p in P[ 0 : numPoints ] ], color=[ color( c ) for c in clusterId ], s=10 )

plt.show()
