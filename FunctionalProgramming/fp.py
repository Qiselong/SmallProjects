## Date 16.01.23

# Objectives: programs the functions described in Introduction to Functional Programming by Bird & Walker

import random

def main():
    L = [[1,2], [3],[4,5,6]]
    print(L)
    res = concat(L)
    print(res)

def and_list(L):
    def and_op(a,b):
        return a and b
    return foldr(and_op, True, L)

def or_list(L):
    def or_op(a,b):
        return a or b
    return foldr(or_op, False, L)

def concat(L):
    def concat_op(a,b):
        return a+b
    return foldr(concat_op, [], L)

def sum(L):
    def sum_op(a,b):
        return a+b
    return foldr(sum_op, [0], L)

def product(L):
    def product_op(a, b):
        return a*b
    return foldr(product_op, 1, L)

def swap(elt, L): #currently not working
    ### returns a list
    # elt is to be put at 1st or 2nd place
    if elt <= L[0]:
        return [elt] + L
    if elt > L[0]:
        if len(L)>1:
            return [L[0]]+[elt]+L[:1]
        else:
            return [L[0]]+ [elt]


def foldr(f, a, L):
    for i in range(len(L)-1, -1, -1):
        #print('i', i, 'a',a, 'L', L)
        a = f(L[i], a)
    return a

main()