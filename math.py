# Add implementation
def add(x,y):
    return x+y

# subtract implementation
def subtract(x,y):
    return x-y #in master
def multiply(x,y):
    return x*y #in bug4 branch
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return DIVIDE_BY_0_ERROR #rebase conflict resolved

def square(x):
    return x*x
