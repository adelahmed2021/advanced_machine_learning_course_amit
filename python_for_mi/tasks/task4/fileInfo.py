class TextFileReader:
    def __init__(self,file_path):
        self.file_path = file_path
        f=open(self.file_path,'r')
        self.file= f.readlines()
    def count_lines(self):
        return len(self.file)

    def count_words(self):
        count=0
        for i in self.file:
            count+=len(i.split())
        return count
    def count_characters(self):
        count=0
        for i in self.file:
            count+=len(i)
        return count
    def display_content(self):
        for i in self.file:
            print(i,end = '')

if __name__=='__main__':
    tf=TextFileReader(r'C:\Users\Lenovo\Desktop\AMIT\advanced_machine_learning_course_amit\python_for_mi\tasks\task4\testFileInfo.txt')
    print("number of lines = "+str(tf.count_lines()))
    print("number of words = "+str(tf.count_words()))
    print("number of characters = " + str(tf.count_characters()))
    tf.display_content()