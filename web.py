import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n' #session_state some kind of dictionary. It looks like a dictionary, but not exactly
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo, key="new_todo") #label can be "" empty

st.session_state