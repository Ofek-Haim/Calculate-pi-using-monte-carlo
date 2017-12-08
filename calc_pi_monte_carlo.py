"""
Ofek Haim
1.5.2017
v 1.0.3
Python 2
"""

from random import random

MULTIPLES = 1


def return_two_random_numbers():
    return random(), random()


def calc_pi_monte_carlo():
    inside_the_circle = 0
    for run in xrange(MULTIPLES):
        x, y = return_two_random_numbers()
        print str(x) + " -- " + str(y)
        if (x * x) + (y * y) < 1:
            inside_the_circle += 1
    pi = 4.0 * inside_the_circle / MULTIPLES
    print "Pi is %s " % str(pi)


if __name__ == '__main__':
    calc_pi_monte_carlo()
