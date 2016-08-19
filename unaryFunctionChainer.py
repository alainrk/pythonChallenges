# Higher order function for chaining together a list of unary functions. In other words, it should return a function that does a left fold on the given functions

def chained(functions):
    return lambda x: reduce(lambda g,f: f(g), functions, x) 
