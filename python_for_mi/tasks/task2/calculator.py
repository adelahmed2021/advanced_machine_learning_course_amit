#validation layer for input
def clear_any_space(eq):
    result=''
    for i in eq:
        if i==' ':
            continue
        else:
            result+=i
    return result

def put_space(eq):
    result=''
    operator=['+','-','*','/']
    for i in eq:
        if i in operator:
            result+=' '
            result+=i
            result+=' '
        else:
            result+=i
    result=result
    return result

def validation_input(eq):
    operator=['+','-','*','/']
    numbers=['0','1', '2', '3','4','5','6','7','8','9']
    for i in eq:
        if i==' ' or i in numbers or i in operator:
            pass
        else:
            return False
    return True

def operator_after_operator(eq):
    operator=['+','-','*','/']
    lst=eq.split()
    for i in range(0,len(lst)):
        if lst[i] in operator and (lst[i+1] in operator):
                return False
    return True

def scan_input():
    eq=input('please enter your equation, and if you want exit enter exit: ')
    eq=clear_any_space(eq)
    eq=put_space(eq)
    return eq

def start_or_end_operator(eq):
    operator=['+','-','*','/']
    if eq[0] in operator or eq[len(eq)-1] in operator:
        return False
    return True

# logic functions
sum = lambda x,y: x+y
sub = lambda x,y: x-y
mul = lambda x,y: x*y
dev = lambda x,y: x/y

def contains_operator_mul_dev(eq,op):
    i=eq.index(op)-1
    if op=='*':
        z=mul(int(eq[i]),int(eq[i+2]))
    if op=='/':
        z=dev(int(eq[i]),int(eq[i+2]))
    eq.pop(i)
    eq.pop(i)
    eq.pop(i)
    eq.insert(i,z)
    return eq

def handle_mul_and_dev_operator(eq):
    eq=eq.split()
    while '*'in eq :
        eq=contains_operator_mul_dev(eq,'*')
    while '/'in eq :
        eq=contains_operator_mul_dev(eq,'/')
    return eq

def final_result(eq):
    i=0
    result=0
    if len(eq)==1:
        return eq
    operator=['+','-']
    flag=False
    while len(eq)>1:
        if eq[1] == '+':
            result=sum(int(eq[0]),int(eq[2]))
            eq.pop(0)
            eq.pop(0)
            eq.pop(0)
            eq.insert(0,result)
            result=eq
        elif eq[1] == '-':
            result=sub(int(eq[0]),int(eq[2]))
            eq.pop(0)
            eq.pop(0)
            eq.pop(0)
            eq.insert(0,result)
            result=eq
    return result


# run code ==> main function
eq=scan_input()
while True:
    if eq =='exit':
        print('good bay')
        exit()
    if  not validation_input(eq) or not operator_after_operator(eq) or not start_or_end_operator(eq):
        print(f'this equation {eq} is valid, please enter your equation again')
        eq=scan_input()
    else:
        eq=handle_mul_and_dev_operator(eq)
        eq=final_result(eq)
        print(eq)
        eq=scan_input()