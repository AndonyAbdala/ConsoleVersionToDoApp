while True: 
    user_prompt = input("Type add, edit, show, complete or exit: ")
    user_prompt = user_prompt.strip()
    match user_prompt:
        case "add":
            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            todo_item = input("Enter a todo: ") + "\n"
            todo_list.append(todo_item)

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)
        case "show":
            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            for index, todo_element in enumerate(todo_list):
                todo_element = todo_element.strip("\n")
                print(f"{index + 1}.- {todo_element.capitalize()}")
        case "edit":
            item_index = int(input("Enter the number of item you want to modify: "))
            item_index = item_index - 1
            value = input("Enter the new todo: ")

            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            todo_list[item_index] = value + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)
        case "complete":
            item_index = int(input("Enter the number of item you have completed: "))

            with open('todos.txt', 'r') as file:
                todo_list = file.readlines()

            todo_list.pop(item_index - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todo_list)

            print("Pending activities: ")
            for index, todo_element in enumerate(todo_list):
                print(f"{index + 1}.- {todo_element.strip("\n").title()}")
        case "exit":
            print("Good bye!")
            break
        case _:
            print("You entered an unknown command")