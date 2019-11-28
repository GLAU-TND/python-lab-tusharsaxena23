class MyException(Exception):
    def __init__(self,v):
        self.v=v
def xyz():
    a=30
    b=40
    sum=a+b
    if sum<150:
        raise MyException('Custom Exception Occurred')
xyz()
