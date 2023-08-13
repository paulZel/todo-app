import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo") #usuall empty
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20)) #layout expects a list of lists double breckets

# each row in new list
while True:
    event, values = window.read() #this method will display window on the screen
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()