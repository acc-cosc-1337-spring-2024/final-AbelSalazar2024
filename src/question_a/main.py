#add import
#Question 1 -- Enter a series of 5 numbers

from question_a import calculate_lowest, calculate_highest, calculate_total, calculate_average

def get_numbers():
    numbers = []
    for _ in range(5):
        number = int(input("Enter a number: "))
        numbers.append(number)
    return numbers

def main():
    numbers = get_numbers()
    print("Lowest number:", calculate_lowest(numbers))
    print("Highest number:", calculate_highest(numbers))
    print("Total:", calculate_total(numbers))
    print("Average:", calculate_average(numbers))

main()
