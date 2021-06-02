# Create a compose function to carry out this task, which will be passed two functions or lambdas.

import inspect
    
def compose(f, g):
    t = tuple(inspect.getargspec(g)[0])
    return lambda *t: f(g(*t))
