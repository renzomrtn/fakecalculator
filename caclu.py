import random

def calculator():
  while True:
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice =  input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("K bye")
    break

    if choice in ['1', '2', '3', '4']:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))

    if choice == '1':
        result = random.randint(1, 1000)
    elif choice == '2':
      result = random.randint(-10000, 10000)
    elif choice == '3':
      result = random.randint(1, 10000) * num1 * num2
    elif choice == '4':
      result = random.choice([x for x in range (-10000, 10000) if x!=0])

    print(f"Result: {result}")
  else:
    print("Invalid choice. Please select a valid option.")

if __name__== "__main__":
  calculator()
  
