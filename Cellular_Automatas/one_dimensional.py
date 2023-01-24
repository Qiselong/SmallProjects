from PIL import Image
import numpy as np
import random

###### PARAMS
n = 1000
N = 1000
rules = 54

# Idea: study Wolframs' rule for 1 domensional cellular automata namely
# produce images of the propagation of these rules. 

# one configuration is given by a n by 1 matrix (list) of binary numbers. 
# We have 8 rules determining how the propagation is happening. Each rule is of the form f(b_1 b_2 b_3) = b. 

# We simulate N steps on a size n torus. For simplicity we work first on a nxN matrix. At each step we look at the line 
# atop of it.
# 

##### MAIN

def main():
    Mat = np.zeros((N, n))
    s_0 = random_config(n)

    Mat[0] = s_0
    rules_b = f_rules_b(rules)
    rule = rules
    i = 1
    while i - N != 0:
        next_line(i, rules_b,Mat)
        i+=1
    Mat = Mat*255
    img = Image.fromarray(Mat)
    img.show()


    
###### TOOLS
def random_config(n):
    return [np.random.randint(0,2) for i in range(n)]

def f_rules_b(rules):
    """return rules (in binary)"""
    rules_b  = bin(rules)[2:]
    while len(rules_b) != 8:
        rules_b = '0' + rules_b
    return rules_b

def next_line(i, rules_b, Mat):
    """fills line i."""
    for x in range(n):
        Neigh_x = [Mat[i-1, (x+j)%n] for j in [-1, 0, 1]]# get neighborhood 
        Mat[i, x] = f_rules(Neigh_x, rules_b)

def f_rules(neigh, rules_b):
    token = 0
    if neigh == [1,1,1]:
        token = 0
    elif neigh == [1,1,0]:
        token = 1
    elif neigh == [1,0,1]:
        token = 2
    elif neigh == [1,0,0]:
        token = 3
    elif neigh == [0,1,1]:
        token = 4
    elif neigh == [0,1,0]:
        token = 5
    elif neigh == [0,0,1]:
        token = 6
    else: token = 7
    return rules_b[token]
    
def gen(Mat):
    N = len(Mat)
    n = len(Mat[0])


###### EXEC
main() 