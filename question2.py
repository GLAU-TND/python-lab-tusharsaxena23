class MyException(Exception):
    def __init__(self,v):
        self.v=v
def exceptionhandling():
    a=10
    try:
        a+='abc'
    except TypeError as e:
        print(e)
    try:
        a.abcd()
    except AttributeError as e:
        print(e)
    try:
        int('sd')
    except ValueError as e:
        print(e)
    
exceptionhandling()
    
