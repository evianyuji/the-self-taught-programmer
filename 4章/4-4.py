def first(fir):
    '''
    Returns fir / 2.
    :param fir:int.
    :return The value obtained by dividing a by 2.
    '''
    
    return fir / 2

def second(sec):

    '''
    Returns sec * 4.
    :param sec:int
    return sec value multiplied by 4.
    '''
    
    return sec * 4

a = input("input a number:")
a = int(a)

retA = first(a)
retA = int(retA)
retB = second(retA)
retB = int(retB)

print(retB)
