def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "undo":
            if history:
                undone = history.pop()
                print(f"Undone: '{undone}'")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)

        print(history)


main()
# def calculate_index(lst):
#     sum = 0
#     for i in range(len(lst)):
#         sum += i
#     print(sum)
#     return round(sum / len(lst))

# print(calculate_index(["up", "down", "left", "right"]))


    
