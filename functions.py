FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list 
    of to-do items.
    """ #docstring info about the function. For example in help(len)

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


#print(help(get_todos))


#def write_todos(todos_arg, filepath="todos.txt"): #in function definition we call them parameters
def write_todos(todos_arg, filepath=FILEPATH): #in function definition we call them parameters
    """ Write the todos item list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
