def method(f):
    '''
    Convert the input value to the float type and display it on the screen.
    :param f:str
    '''
    
    try:
        fVal = float(f)
        print(fVal)
    except ValueError:
        print("input Integer please!")

a = input("input a number:")
method(a)


        
