#add import

import question_b

while True:
    print("\nMenu")
    print("1 - Display purchase stock history")
    print("2 - Exit menu")

    select = input("Select a number: ")

    while select not in ("1", "2"):
        select = input("Invalid number: Select 1 or 2: ")

    if select == "1":
        print("Purchase stock history")
        question_b.stock_purchase_history()

    if select == "2":
        print("Exiting program.")
        break

