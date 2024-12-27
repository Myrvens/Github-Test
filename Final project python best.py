import random

def calculate_lcm(num1, num2):
    # Calculate the Least Common Multiple (LCM) of two numbers.
    lcm = max(num1, num2)
    while True:
        if lcm % num1 == 0 and lcm % num2 == 0:
            return lcm
        lcm += 1

def calculate_gcf(num1, num2):
    # Calculate the Greatest Common Factor (GCF) of two numbers.
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def find_multiples(num):
    # Find multiples of a number up to 30.
    multiples = []
    for i in range(1, 31):
        multiple = num * i
        if multiple <= 30:
            multiples.append(multiple)
    return multiples

def main():
    while True:
        print("\nMenu:")
        print("1. Calculate LCM")
        print("2. Calculate GCF")
        print("3. Find Multiples")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(f"LCM of {num1} and {num2} is {calculate_lcm(num1, num2)}")
        elif choice == '2':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(f"GCF of {num1} and {num2} is {calculate_gcf(num1, num2)}")
        elif choice == '3':
            num = int(input("Enter a number: "))
            print(f"Multiples of {num} up to 30 are: {find_multiples(num)}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()