#https://mdecourse.github.io/twolink_ik/two_link_ik_Notebooks.html
from sympy import *
import math
from sympy.solvers import solve

# FK
t1 = Symbol('theta_1')
t2 = Symbol('theta_2')
L1 = Symbol('L_1')
L2 = Symbol('L_2')
u = L1 * sin(t1)
v = L1 * cos(t1)
#print([u, v])
x = u + L2 * sin(t1+t2)
y = v + L2 * cos(t1+t2)
#print([x, y])
# [L_1*sin(theta_1) + L_2*sin(theta_1 + theta_2), L_1*cos(theta_1) + L_2*cos(theta_1 + theta_2)]

#IK
i = expand(x**2 + y**2)
#print(i)
j = simplify(i)
print(j)
x2 = Symbol('x')
y2 = Symbol('y')
j2 = (x2**2 + y2**2)
print(j2)
k = solve(j2 - j, t2)
#print(k)
# t2 = [-acos(-(L_1**2 + L_2**2 - x**2 - y**2)/(2*L_1*L_2)) + 2*pi, acos((-L_1**2 - L_2**2 + x**2 + y**2)/(2*L_1*L_2))]
# law of cosine
alpha = atan(y2/x2)
#print(alpha)
beta = pi / 2 - t1 - alpha
print(beta)
beta2 = atan((L2 * sin(t2))/(L1 + L2 * cos(t2)))
print(beta2)
k2 = solve(beta2 - beta, t1)
#print(k2)
# t1 = [-atan(y/x) - atan(L_2*sin(theta_2)/(L_1 + L_2*cos(theta_2))) + pi/2]








