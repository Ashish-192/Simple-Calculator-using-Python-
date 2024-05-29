def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return "Error: Cannot divide by zero."
  else:
    return x / y

def power(x, y):
  return x ** y

def modulo(x, y): #Performs modulo operation and returns the remainder.
  if y == 0:
    return "Error: Modulo by zero."
  else:
    return x % y

while True:
  num1 = float(input("Enter the first number: "))
  operator = input("""Choose operation (+, -, *, /, ^ (power), %% (modulo)): """)
  num2 = float(input("Enter the second number: "))

  result = None
  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  elif operator == "^":
    result = power(num1, num2)
  elif operator == "%":
    result = modulo(num1, num2)
  else:
    print("Invalid operator. Please choose +, -, *, /, ^, or %.")
    continue

  if result:
    print(f"{num1} {operator} {num2} = {result}")

  choice = input("Do you want to perform another calculation? (y/n): ")
  if choice.lower() != "y":
    break
print("Calcualtor Closed.")