# message = "Enter a to do: "
# todo1 = input(message)
# todo2 = input(message)
# todo3 = input(message)

# todos = [todo1, todo2, todo3]
# print(todos)
# print(type(todos))
# print(type(todo1))

# text = input("Enter something: ")
# print("Number of letters is: " + str(len(text)))

todo_list = []

while True: 
    user_prompt = input("Type add, edit, show or exit: ")
    user_prompt = user_prompt.strip()
    match user_prompt:
        case "add":
            todo_item = input("Enter a todo: ")
            todo_list.append(todo_item)
        case "show":
            for todo_element in todo_list:
                print(todo_element)
        case "edit":
            item_index = int(input("Enter the number of item you want to modify: "))
            item_index = item_index - 1
            value = input("Enter the new todo: ")
            todo_list[item_index] = value
        case "exit":
            print("Good bye!")
            break
        case _:
            print("You entered an unknown command")