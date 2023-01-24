import cv2
import numpy as np
import random

get_bin = lambda x, n: format(x, 'b').zfill(n)

def cprint(img, name='default', time = 5000):
    """ custom print; 5 sec."""
    cv2.imshow(name, img)
    cv2.waitKey(time)

def StB(message):
    "convert a message (string) to a sequence of bits."
    seq = ''
    for i in range(len(message)):
        c = ord(message[i])
        seq += str(get_bin(c, 8))
    return seq

def imprint(message, img):
    """modifies img with message."""
    # 1: get the bit sequence
    seq = StB(message)


    # 2: starting positon
    p0 = [0,0]
    shp = img.shape
    lx ,ly= shp[1], shp[0]

    # 3: 
    pos = p0
    for b in seq:
        col = img[pos[0]][pos[1]]
        #print('col, ', col)
        img[pos[0]][pos[1]] = colchange(col, b)
        pos = nextP(pos, lx, ly)
    
    return img
        


def nextP(pos, lx, ly):
    """ determines the position of the next pixel."""
    pos[1] += 1
    if pos[1] >= lx:
        pos[1] = 0
        pos[0] +=1
    return pos

def colchange(col, b):
    if b=='1':
        pool = []
        for i in range(3):
            if col[i] < 255:
                pool.append(i)
    else:
        pool = []
        for i in range(3):
            if col[i] > 0:
                pool.append(i)
    r = random.choice(pool)
    if b == '1':
        col[r] +=1
    else:
        col[r] += -1
    #print(r, col)
    return col

def BtS(sequence):
    "convert a sequence of bits to a string"

def difference(img1, img2):
    '''observe the difference between img1 and img2. return a grayscale image. 0 means -1, 200 means 1, 100 means no change.'''

    def pdiff(col1, col2):
        return sum([col1[i] - col2[i] for i in range(3)])

    lx, ly = img1.shape[1], img1.shape[0]
    img3 = np.zeros_like((ly, lx))
    for x in range(lx):
        for y in range(ly):
            col1, col2 = img1[y][x], img2[y][x]
            print(col1, col2)
            img3[y][x] += 100 + 100*pdiff(col1, col2)
    return img3

