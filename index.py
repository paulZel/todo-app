#todos = []

#from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print("It is: ", now)
while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip() # 'add ', нам потрібно 'add' без пробела
    #this is a string

    #if 'add'in user_action or 'new' in user_action or 'create' in user_action:
    if user_action.startswith("add"):
        todo = user_action[4:]

        #file = open('todos.txt', 'r')
        #todos = file.readlines()
        #file.close()

        #Це безпечніше і краще ніж вище, файл буде закритий автоматично any case

        todos = functions.get_todos(filepath="todos.txt") #The argument value
        #this is a module

        todos.append(todo + '\n')

        #file = open('todos.txt', 'w')
        #file.writelines(todos)
        #file.close()
        #with open('todos.txt', 'w') as file:
          #  file.writelines(todos)
        #write_todos(todos_arg=todos, filepath="todos.txt") # the argument value

        functions.write_todos(todos, "todos.txt") # the argument value   #the filepath default it's not necessary to pass




    elif user_action.startswith("show"):
        #print(todos)

        #file = open('todos.txt', 'r')
        #todos = file.readlines() #контент уже в этой переменной
        #file.close()

        todos = functions.get_todos("todos.txt")

        #new_todos = []

        #for item in todos:
            #new_item = item.strip('\n')
            #new_todos.append(new_item)

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            #item = item.strip('\n')
            item = item.capitalize()
            #print(index, '.', item) #Для контролю над цією строкою нам потрібно f string
            row = f"{index + 1}.{item}"
            print(row)
       #print("hello", index, item) the last item of the list will be shown
       #print("length is", index + 1)
       #print(f"length is {index + 1}")
        #print(len(todos))
    elif user_action.startswith("edit"):
        try:
            #number = int(input("Number of the to do to edit: "))
            number = int(user_action[5:]) #від користувача отимуэмо str
            number = number - 1

            todos = functions.get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            #number = int(input("Number of the to do to complete: "))
            number = int(user_action[9:])

            todos = functions.get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    #elif 'exit' in user_action:
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")


#todo1 = input(user_prompt)
#todo2 = input(user_prompt)
#todo3 = input(user_prompt)

#todos = [todo1, todo2, todo3, "hello"]
#print(todos)


