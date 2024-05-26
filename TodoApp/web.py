import streamlit as st
import functions

todos = functions.get_todos(r"TodoApp\todos.txt")


def add_todo():
    todo_local = st.session_state["new_todo"].title() + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My To-Do App")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a To-Do:", placeholder="Add a new todo:",
              on_change=add_todo, key="new_todo")
