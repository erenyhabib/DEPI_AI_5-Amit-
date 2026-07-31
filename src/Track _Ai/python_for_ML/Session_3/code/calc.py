def add(x:float , y:float):
    '''sum function
    args:
        param_1=user must input the first
        type_param=fleat
        param_2=user must input the first
        type_param=fleat
        type_return=float
        
    '''
    return x+y

def sub(x:float , y:float):
    '''sub function
    args:
        param_1=user must input the first
        type_param=fleat
        param_2=user must input the first
        type_param=fleat
        type_return=float
        
    '''
    return x-y


def div(x:float , y:float):
    '''div function
    args:
        param_1=user must input the first
        type_param=fleat
        param_2=user must input the first
        type_param=fleat
        type_return=float
        
    '''
    return x/y

def mult(x:float , y:float):
    '''mult function
    args:
        param_1=user must input the first
        type_param=fleat
        param_2=user must input the first
        type_param=fleat
        type_return=float
        
    '''
    return x*y

def main():
    print("calc")
    print("=================")
    print("1 add")
    print("2 add")
    print("3 add")
    print("4 add")
    choice=input("enter choice 1 - 2 - 3 -4")
    num=float(input("enter num 1: "))
    num2=float(input("enter num 2: "))

    if choice=='1':
        print(f"first num {num} ,second num {num2}",add(num,num2))
    elif choice=='2':
        print(f"first num {num} ,second num {num2}",sub(num,num2))

    elif choice=='3':
        print(f"first num {num} ,second num {num2}",div(num,num2))
    elif choice=='4':
        print(f"first num {num} ,second num {num2}",mult(num,num2))
        