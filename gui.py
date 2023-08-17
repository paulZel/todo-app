import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text('', key="clock") # don't use module name time in variables
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo") #usuall empty
add_button = sg.Button("Add", size=10) #(size=2, image_source="add.png", mouseover_colors="LightBlue2",
                       #tooltip="Add todo", key="Add") #("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Delete") #(size=2, image_source="complete.png",
                            #tooltip="delete", key="Complete")     #("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20)) #layout expects a list of lists double breckets

# each row in new list
while True:
    event, values = window.read(timeout=200) #this method will display window on the screen
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Delete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0]) # 0 because it's the only item of this list
        case sg.WIN_CLOSED:
            break

window.close()