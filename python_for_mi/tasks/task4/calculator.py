#validation layer for input
class Validation:
    operator=['+','-','*','/']
    numbers=['0','1', '2', '3','4','5','6','7','8','9']
    def __init__(self,eq:str=''):
        self.eq=eq
    
    def clear_any_space(self,eq):
        return eq.replace(' ','')

    def put_space(self,eq):
        result=''
        for i in eq:
            if i in Validation.operator:
                result+=' '
                result+=i
                result+=' '
            else:
                result+=i
        return result

    def validation_input(self,eq):
        for i in eq:
            if i==' ' or i in Validation.numbers or i in Validation.operator:
                pass
            else:
                return False
        return True

    def operator_after_operator(self,eq):
        lst=eq.split()
        for i in range(0,len(lst)):
            if lst[i] in Validation.operator and (lst[i+1] in Validation.operator):
                
                return False
        return True

    def start_or_end_operator(self,eq):
        if eq[0] in Validation.operator or eq[len(self.eq)-1] in Validation.operator:
            return False
        return True

class Logic:
    
    def __init__(self,):
        pass
    sum = lambda x,y: x+y
    sub = lambda x,y: x-y
    mul = lambda x,y: x*y
    dev = lambda x,y: x/y
    
    def contains_operator_mul_dev(eq,op):
        i=eq.index(op)-1
        if op=='*':
            z=Logic.mul(int(eq[i]),int(eq[i+2]))
        if op=='/':
            z=Logic.dev(int(eq[i]),int(eq[i+2]))
        eq.pop(i)
        eq.pop(i)
        eq.pop(i)
        eq.insert(i,z)
        return eq

    def handle_mul_and_dev_operator(self,eq):
        eq=eq.split()
        while '*'in eq :
            eq=Logic.contains_operator_mul_dev(eq,'*')
        while '/'in eq :
            eq=Logic.contains_operator_mul_dev(eq,'/')
        return eq

    def final_result(self,eq):
        i=0
        result=0
        if len(eq)==1:
            return eq
        while len(eq)>1:
            if eq[1] == '+':
                result=Logic.sum(int(eq[0]),int(eq[2]))
                eq.pop(0)
                eq.pop(0)
                eq.pop(0)
                eq.insert(0,result)
                result=eq
            elif eq[1] == '-':
                result=Logic.sub(int(eq[0]),int(eq[2]))
                eq.pop(0)
                eq.pop(0)
                eq.pop(0)
                eq.insert(0,result)
                result=eq
        return result


if __name__ == '__main__':
    while True:
        eq=input('enter your equation, or write exit if you wont terminate: ')
        if eq == 'exit':
            break
        val=Validation(eq)
        eq=val.clear_any_space(eq)
        eq=val.put_space(eq)
        f1=val.start_or_end_operator(eq)
        f2=val.operator_after_operator(eq)
        f3=val.validation_input(eq)
        if not (f1 and f2 and f3):
            print('invalid input please try again (-_-)')
            continue
        equation = Logic()
        eq=equation.handle_mul_and_dev_operator(eq)
        result=equation.final_result(eq)
        print(result)










