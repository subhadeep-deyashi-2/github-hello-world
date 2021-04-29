# Add implementation
def add(x,y):
    return y+x

# subtract implementation
def subtract(x,y):
    return x-y #in master
    
# multiplication implementation
def multiply(x,y):
    return x*y #in bug4 branch
    
# division implementation
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return DIVIDE_BY_0_ERROR #rebase conflict resolved

# square implementation
def square(x):
    return x*x
