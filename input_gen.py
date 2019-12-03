import numpy as np

print "<< --- 2D STRESS ANALYSIS USING QUAD --- >>"
print "PROBLEM 0.0"

print "<< NN NE NM NDIM NEN NDN >>"
print "33 20 1 2 4 2"	
print "<< ND NL NMPC >>"	
print "6 1 0"

print "<< Node# Coordinates >>"
node_nums = np.arange(1,34)
for n in node_nums:
	print n, ((n-1)//3)*.01, ((n-1)%3)*.005

print "<< Elem# Nodes Mat# Thickness TempRise >>"
elem_nums = np.arange(1,21)
for e in elem_nums:
	left_top = e + e//2 + e%2
	print e, left_top - 1, left_top + 2, left_top + 3, left_top, 1, 1, 0 

print "<< DOF# Displacement >>"
for i in np.arange(1,7):
	print i,0

print "<< DOF# Load >>"
print 66, -1000
print "<< MAT# E Nu Alpha >>"
print 1, 1E9, 0.499, 12E-6
print "B1 i B2 j B3 (Multi-point constr. B1*Qi+B2*Qj=B3)"

