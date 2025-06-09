while True: 
    user_prompt = input("Type add, edit, show, complete or exit: ")
    user_prompt = user_prompt.strip()
    match user_prompt:
        case "add":
            file = open('todos.txt', 'r')
            todo_list = file.readlines()
            file.close()

            todo_item = input("Enter a todo: ") + "\n"
            todo_list.append(todo_item)

            file = open('todos.txt', 'w')
            file.writelines(todo_list)
            file.close()
        case "show":
            file = open('todos.txt', 'r')
            todo_list = file.readlines()
            file.close()

            for index, todo_element in enumerate(todo_list):
                todo_element = todo_element.strip("\n")
                print(f"{index + 1}.- {todo_element.capitalize()}")
        case "edit":
            item_index = int(input("Enter the number of item you want to modify: "))
            item_index = item_index - 1
            value = input("Enter the new todo: ")
            todo_list[item_index] = value
        case "complete":
            item_index = int(input("Enter the number of item you have completed: "))
            todo_list.pop(item_index - 1)
            print("Pending activities: ")
            for index, todo_element in enumerate(todo_list):
                print(f"{index + 1}.- {todo_element}")
        case "exit":
            print("Good bye!")
            break
        case _:
            print("You entered an unknown command")