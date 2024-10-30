def read_txt_file(file_path):
    """Reads the contents of a text file and returns it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().splitlines()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except IOError:
        return "Error: An error occurred while reading the file."

class UserExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file=read_txt_file(self.file_path)

    def extract_usernames(self):
        """Extracts usernames from the text file and stores them in a dictionary."""
        users=[]
        for i in self.file:
            users.append(i.split(":")[0])
        return users
# Usage example
if __name__ == "__main__":
    file_path = r'C:\Users\Lenovo\Desktop\AMIT\advanced_machine_learning_course_amit\python_for_mi\tasks\task4\testTask6.txt'
    u=UserExtractor(file_path)
    print(u.extract_usernames())