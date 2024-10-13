email='Amit_ml@gmail.edu'
flag =True
if email.count('@') != 1 and email.count('.') < 1:
    flag = False 
    print("Invalid email")
else:
    user=email.split('@')[0]
    domain=email[email.index('@')+1: email.index('.')]
if flag:
    if email.endswith('.com'):
        print('Commercial Domain')
    elif email.endswith('.edu'):
        print('Educational Domain')
    else:
        print('Other Domain')