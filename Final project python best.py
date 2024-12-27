import random

def calculate_lcm(num1, num2):
    """Calculate the Least Common Multiple (LCM) of two numbers."""
    # First, find the GCF
    gcf = calculate_gcf(num1, num2)
    # Use the formula to calculate LCM
    lcm = (num1 * num2) // gcf
    return lcm

def calculate_gcf(num1, num2):
    """Calculate the Greatest Common Factor (GCF) of two numbers."""
    while num2 != 0:
        # Swap and reduce using modulus
        num1, num2 = num2, num1 % num2
    return num1

def find_multiples(num, limit=30):
    """Find multiples of a number up to the specified limit."""
    multiples = []
    for i in range(1, limit + 1):
        multiple = num * i
        if multiple > limit:
            break
        multiples.append(multiple)
    return multiples

def find_factors(num):
    """Find all factors of a number."""
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# Main program loop
while True:
    # Generate two random integers between 2 and 30
    num1 = random.randint(2, 30)
    num2 = random.randint(2, 30)

    # Display the generated numbers
    print("Generated Numbers:")
    print(f"Integer 1: {num1}")
    print(f"Integer 2: {num2}")
    print()

    # Find and display multiples for both numbers
    print(f"Finding multiples of {num1}...")
    multiples_of_num1 = find_multiples(num1)
    print(f"Multiples of {num1}: {multiples_of_num1}")

    print(f"Finding multiples of {num2}...")
    multiples_of_num2 = find_multiples(num2)
    print(f"Multiples of {num2}: {multiples_of_num2}")
    print()

    # Calculate and display the LCM
    print("Calculating the Least Common Multiple (LCM)...")
    lcm = calculate_lcm(num1, num2)
    print(f"The Least Common Multiple of {num1} and {num2} is: {lcm}")
    print()

    # Find and display factors for both numbers
    print(f"Finding factors of {num1}...")
    factors_of_num1 = find_factors(num1)
    print(f"Factors of {num1}: {factors_of_num1}")

    print(f"Finding factors of {num2}...")
    factors_of_num2 = find_factors(num2)
    print(f"Factors of {num2}: {factors_of_num2}")
    print()

    # Calculate and display the GCF
    print("Calculating the Greatest Common Factor (GCF)...")
    gcf = calculate_gcf(num1, num2)
    print(f"The Greatest Common Factor of {num1} and {num2} is: {gcf}")
    print()

    # Ask the user if they want to continue
    try_again = input("Press Enter to try again, or type 'exit' to stop: ").strip().lower()
    if try_again == "exit":
        print("Thank you for using the program. Goodbye!")
        break
    print("-" * 40)
    print()
