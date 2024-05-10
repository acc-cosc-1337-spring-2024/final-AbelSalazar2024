#add import

import question_d

while True:
    print("\nMenu")
    print("1 - Create table")
    print("2 - Exit menu")

    select =  str(input ("Select a number: "))

    while select not in ("1" , "2"):
        select = str(input("Invalid number: Select 1 or 2:  "))

    if select ==  "1":
        Row = int(input("Number of rows : "))
        colum = int(input("Number of columns :  "))

        table = question_d.create_multiplication_table(Row, colum)
        
        question_d.display_multiplication_table(table)
    elif select == "2":
        print ("Exiting the program.")
        break