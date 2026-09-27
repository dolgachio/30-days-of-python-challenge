def some_func():
    hey = not 33 or not 44
    
    print('------', hey)
    
    print('not-----', '0:', bool(0), '1:', bool(1), '{}', bool({}), '()', bool(()), 'None: ', bool(None))
    
    print('-----range', type(range(1, 10)))
    
    return 1, 2, 3

print('-----', type(some_func()))