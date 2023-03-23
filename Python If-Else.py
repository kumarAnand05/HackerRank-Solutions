#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    s1 = 'Weird'
    s2 = 'Not Weird'

    if n%2 ==0 and (n in range(2,6) or n>20): print(s2)
    else: print(s1)
