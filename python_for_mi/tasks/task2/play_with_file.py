import os
import random
folder=os.mkdir(r"C:\Users\Lenovo\Desktop\AMIT\advanced_machine_learning_course_amit\python_for_mi\testFolder")
path=r"C:\Users\Lenovo\Desktop\AMIT\advanced_machine_learning_course_amit\python_for_mi\testFolder"
if os.path.exists(path):
    print('exists')
else:
    folder=os.mkdir(r"C:\Users\Lenovo\Desktop\AMIT\advanced_machine_learning_course_amit\python_for_mi\testFolder")

for i in range(20):
    open(os.path.join(path,fr'{i}.txt'),'w')
count = len(os.listdir(path))
print(count)

while len(os.listdir(path)) > count/2:
    z=random.randint(0,20)
    if os.path.exists(rf"C:\Users\Lenovo\Desktop\AMIT\advanced_machine_learning_course_amit\python_for_mi\testFolder\{z}.txt"):
        os.remove(rf"C:\Users\Lenovo\Desktop\AMIT\advanced_machine_learning_course_amit\python_for_mi\testFolder\{z}.txt")
print(len(os.listdir(path)))