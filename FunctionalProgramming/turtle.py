## date 16.01.23

#objective: implementation of the turtle described in (...)

import copy

#init
init = [0, False, 0, 0]

def main():
    program = 'down move up move move down move right move move move'
    states = unwrap(program)
    tr = trail(states)
    bmp = bitmap(tr)
    img = symbolic(bmp)
    save(img)

def save(img):
    file = open('FunctionalProgramming/img.txt', 'w')
    for line in img:
        file.write(line +'\n')
    file.close()

def symbolic(bmp):
    t = 'O'
    f = '.'
    image = []
    for line in bmp:
        l = ''
        for val in line:
            if val:
                l+=t
            else:
                l+=f
        image.append(l)
    return image

def bitmap(ps):
    minx, maxx = ps[0][0], ps[0][0]
    miny, maxy = ps[0][1], ps[0][1]
    for p in ps:
        minx = min(minx, p[0])
        miny = min(miny, p[1])
        maxx = max(maxx, p[1])
        maxy = max(maxy, p[1])
    rangeX, rangeY = range(minx, maxx +1), range(miny, maxy+1)
    return [[(x,y) in ps for x in rangeX] for y in rangeY]

def trail(successive_states):
    ''' given the successive states, output positions where the pen was down'''
    return [(x,y) for (d, p, x, y) in successive_states if p == True ]

def unwrap(program):
    """ unwrap the program as a list of command separated by ' '. Outputs the list of states."""
    successive_states= [init]
    for c in program.split(' '):
        state = successive_states[-1]
        new_state = command(c, state)
        successive_states.append(new_state)
    return successive_states

def command(c, S):
    """ compute next state given a command name and a state"""
    if c == 'move':
        return move(S)
    if c == 'right':
        return right(S)
    if c == 'left':
        return left(S)
    if c == 'up':
        return up(S)
    if c == 'down':
        return down(S)

def move(S):
    Next = S.copy()
    if S[0]==0: 
        Next[2]=S[2]-1
        return Next
    elif S[0] == 1:
        Next[3] = S[3] + 1
        return Next
    elif S[0] == 2:
        Next[2] += 1
        return Next
    else:
        Next[3] += -1
        return Next

def right(S):
    N = S.copy()
    N[0] = (S[0]+1)%4
    return N

def left(S):
    N = S.copy()
    N[0] = (S[0]-1)%4
    return N

def up(S):
    N = S.copy()
    N[1] = False
    return N

def down(S):
    N = S.copy()
    N[1] = True
    return N

main()