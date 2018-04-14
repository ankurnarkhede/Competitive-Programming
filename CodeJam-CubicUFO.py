from math import sin, cos, sqrt, pi
square_by_2 = sqrt(2)
pi_by_2 = pi/2
pi_by_4 = pi/4
T = int(input())
for t in range(1, T+1):
    A = float(input())
    angle = 0
    f = square_by_2*sin(angle + pi_by_4) - A
    deltaaa = 1
    while deltaaa > 1e-12:
        deltaaa = - f/(square_by_2*cos(angle + pi_by_4))
        angle = angle + deltaaa
        f = sqrt(2)*sin(angle + pi_by_4) - A
    x = cos(angle)/2
    y = sin(angle)/2
    print("Case #{}:".format(t))
    print(cos(angle)/2, sin(angle)/2, 0)
    print(cos(angle + pi_by_2)/2, sin(angle + pi_by_2)/2, 0)
print(0, 0, 0.5)