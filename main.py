#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    command = input("Enter your command (add/show/exit/edit/complete): ")
    command = command.strip()

    if command.startswith("add"):
        todo = command[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(filepath="todos.txt", todos_arg=todos)



    elif command.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif command.startswith("edit"):
        try:
            number= int(command[5:])
            print(number)

            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif command.startswith("complete"):
        try:
            number = int(command[9:])

            todos = functions.get_todos("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos("todos.txt", todos)

            message = f"Todo {todo_to_remove} was removed"
            print(message)
        except ValueError:
            print("There is no item with that number")
            continue

    elif command.startswith("exit"):
        break
    else:
        print("Invalid command")



