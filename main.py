import math

def test():
    """
	Test test rteteet
    """
    print(math.sin(0.1))
    

def send(message):
    """
    A method's docstring with parameters and return value.
    
    Use all the cool Sphinx capabilities in this description, e.g. to give
    usage examples ...
    
    :Example:
 
    >>> another_class.foo('', AClass())        
        
    :param arg1: first argument
    :type arg1: string
    :param arg2: second argument
    :type arg2: :class:`module.AClass`
    
    :return: summ
    :rtype: string
    :raises: TypeError
    """
    return 42
 
