# date 22.12.22
# objective:        1. use z3 library to optimize the xp gained given for a profession using a given amount of ressources
#                   2. possible extensions: given level of gathering ressources, provide guideline on what ressources to LF

import z3

def recipe_read():
    '''return as a list of list the recipes.'''
    ingredients=[]
    f=open('dofus/recipe.txt')
    recipes = []
    for line in f:
        b = line.split(';')
        c = [(b[i].split(' ')[0], b[i].split(' ')[1]) for i in range(len(b))]
        recipes.append(c)
        for it in range(len(c)):
            if ingredients.count(c[it][0]) == 0:
                ingredients.append(c[it][0])
    f.close()
    print(ingredients)
    return recipes
    
def private_read(file):
    f=open(file)
    for line in f.readlines():
        print(line)
    f.close()

def private_delete(file):
    f = open(file, 'w')
    f.close()

def add_recipe(string):
    f = open('dofus/recipe.txt', 'a+')
    f.write(string+'\n')
    f.close()

def read_resources(string):
    """ ressources available are in the same format as recipe.txt file. Returns a list of tuples."""    
    b = string.split(';')
    c = [(b[i].split(' ')[0], b[i].split(' ')[1]) for i in range(len(b))]    
    return c

file = 'dofus/recipe.txt'
print(recipe_read())
ressources = 'ash 120;iron 2558'
print(read_resources(ressources))